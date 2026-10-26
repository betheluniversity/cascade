#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export ROOT_DIR
PY36_VERSION="3.6.15"
PYENV_PYTHON="$HOME/.pyenv/versions/$PY36_VERSION/bin/python3.6"
CONFIG_FILE="$ROOT_DIR/config.py"
PACKAGE_NAME="bu-cascade"
PACKAGE_VERSION=""
INDEX_NAME="local"
VENV_DIR="$ROOT_DIR/.venv36"
RUN_DESTRUCTIVE="false"

usage() {
  cat <<'USAGE'
Usage:
  ./scripts/run-tests-py36.sh [options] [pytest args]

Options:
  --index local|test|prod  Package source (default: local)
  --version VERSION        Package version for test/prod index (default: latest)
  --venv-dir PATH          Virtual environment path (default: .venv36)
  --run-destructive        Run destructive integration tests
  -h, --help               Show this help

Examples:
  ./scripts/run-tests-py36.sh
  ./scripts/run-tests-py36.sh --index local --run-destructive
  ./scripts/run-tests-py36.sh --index test --version 3.20 --run-destructive
  ./scripts/run-tests-py36.sh --index prod --version 3.20 -k update_page_c -vv
USAGE
}

PYTEST_ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --index)
      INDEX_NAME="${2:-}"
      shift 2
      ;;
    --version)
      PACKAGE_VERSION="${2:-}"
      shift 2
      ;;
    --venv-dir)
      VENV_DIR="${2:-}"
      shift 2
      ;;
    --run-destructive)
      RUN_DESTRUCTIVE="true"
      PYTEST_ARGS+=("--run-destructive")
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      PYTEST_ARGS+=("$1")
      shift
      ;;
  esac
done

if [[ "$INDEX_NAME" != "local" && "$INDEX_NAME" != "test" && "$INDEX_NAME" != "prod" ]]; then
  echo "Invalid --index value: $INDEX_NAME (use local, test, or prod)" >&2
  exit 1
fi

echo "==> bu-cascade Python 3.6 test runner"
echo "    root: $ROOT_DIR"
echo "    venv: $VENV_DIR"
echo "    index: $INDEX_NAME"
echo "    version: ${PACKAGE_VERSION:-local/latest}"
echo "    mode: $( [[ "$RUN_DESTRUCTIVE" == "true" ]] && echo "destructive (writes enabled)" || echo "non-destructive" )"

if [[ ! -x "$PYENV_PYTHON" ]]; then
  if ! command -v pyenv >/dev/null 2>&1; then
    echo "pyenv is required to install Python $PY36_VERSION." >&2
    echo "Install it with: brew install pyenv" >&2
    exit 1
  fi

  echo "Installing Python $PY36_VERSION with pyenv..."
  pyenv install --skip-existing "$PY36_VERSION"
fi

if [[ ! -f "$CONFIG_FILE" ]]; then
  echo "Missing $CONFIG_FILE" >&2
  echo "Copy config.py.dist to config.py and set SOAP_URL, CASCADE_LOGIN, SITE_ID, and STAGING_DESTINATION_ID." >&2
  exit 1
fi

echo "==> Preflight checks passed"

if [[ ! -d "$VENV_DIR" ]]; then
  echo "Creating virtual environment at $VENV_DIR"
  "$PYENV_PYTHON" -m venv "$VENV_DIR"
fi

"$VENV_DIR/bin/python" - <<'PY'
import importlib.util
import os
import sys

root = os.environ["ROOT_DIR"]
config_path = os.path.join(root, "config.py")
spec = importlib.util.spec_from_file_location("cascade_config", config_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

required = ["SOAP_URL", "CASCADE_LOGIN", "SITE_ID", "STAGING_DESTINATION_ID"]
missing = [name for name in required if not getattr(mod, name, None)]
if missing:
    print("Missing or empty config values: {}".format(", ".join(missing)), file=sys.stderr)
    sys.exit(1)
PY

if [[ "$RUN_DESTRUCTIVE" == "true" ]]; then
  "${VENV_DIR}/bin/python" - <<'PY'
import os
import re
import sys

test_file = os.path.join(os.environ["ROOT_DIR"], "tests", "test.py")
with open(test_file, "r", encoding="utf-8") as f:
    text = f.read()

required_ids = [
    "TEST_PAGE_ID",
    "TEST_BLOCK_ID",
    "TEST_PROGRAM_BLOCK_ID",
    "TEST_FACULTY_PAGE_ID",
    "TEST_METADATA_SET_ID",
    "TEST_DATA_DEFINITION_ID",
]

missing = []
for name in required_ids:
    pattern = rf'^{name}\s*=\s*["\']([^"\']*)["\']\s*$'
    match = re.search(pattern, text, flags=re.MULTILINE)
    if not match or not match.group(1).strip():
        missing.append(name)

if missing:
    print("Missing or empty test IDs in tests/test.py: {}".format(", ".join(missing)), file=sys.stderr)
    print("Set these IDs to real test assets before running with --run-destructive.", file=sys.stderr)
    sys.exit(1)
PY
else
  echo "Note: running without --run-destructive; write/edit tests will be skipped."
fi

"$VENV_DIR/bin/python" -m pip install --upgrade "pip==21.3.1" "setuptools==59.6.0" "wheel==0.37.1"

if [[ "$INDEX_NAME" == "local" ]]; then
  "$VENV_DIR/bin/python" -m pip install ".[test]"
else
  if [[ "$INDEX_NAME" == "test" ]]; then
    INDEX_ARGS=("--index-url" "https://test.pypi.org/simple" "--extra-index-url" "https://pypi.org/simple")
  else
    INDEX_ARGS=("--index-url" "https://pypi.org/simple")
  fi

  if [[ -n "$PACKAGE_VERSION" ]]; then
    PACKAGE_SPEC="${PACKAGE_NAME}==${PACKAGE_VERSION}"
  else
    PACKAGE_SPEC="$PACKAGE_NAME"
  fi

  "$VENV_DIR/bin/python" -m pip install --upgrade "${INDEX_ARGS[@]}" "$PACKAGE_SPEC" "pytest==6.2.5"
fi

cd "$ROOT_DIR"

if [[ "$INDEX_NAME" == "local" ]]; then
  echo "==> Import mode: local src/ tree"
else
  echo "==> Import mode: installed package"
  CASCADE_USE_INSTALLED_PACKAGE=1 "$VENV_DIR/bin/python" -c 'import bu_cascade; print(bu_cascade.__file__)'
fi

echo "==> Collecting tests"
if [[ "$INDEX_NAME" == "local" ]]; then
  PYTHONPATH=src "$VENV_DIR/bin/python" -m pytest --collect-only -q tests/test.py "${PYTEST_ARGS[@]}"
else
  CASCADE_USE_INSTALLED_PACKAGE=1 "$VENV_DIR/bin/python" -m pytest --collect-only -q tests/test.py "${PYTEST_ARGS[@]}"
fi

has_verbosity_arg="false"
for arg in "${PYTEST_ARGS[@]:-}"; do
  if [[ "$arg" == "-q" || "$arg" == "--quiet" || "$arg" == "-v" || "$arg" == "-vv" || "$arg" == "--verbose" ]]; then
    has_verbosity_arg="true"
    break
  fi
done

pytest_flags=("-ra")
if [[ "$has_verbosity_arg" == "false" ]]; then
  pytest_flags+=("-v")
fi

echo "==> Running tests"
set +e
if [[ "$INDEX_NAME" == "local" ]]; then
  PYTHONPATH=src "$VENV_DIR/bin/python" -m pytest "${pytest_flags[@]}" tests/test.py "${PYTEST_ARGS[@]}"
else
  CASCADE_USE_INSTALLED_PACKAGE=1 "$VENV_DIR/bin/python" -m pytest "${pytest_flags[@]}" tests/test.py "${PYTEST_ARGS[@]}"
fi
pytest_exit=$?
set -e

if [[ $pytest_exit -eq 0 ]]; then
  echo "==> SUCCESS: pytest completed with exit code 0"
else
  echo "==> FAILURE: pytest exited with code $pytest_exit" >&2
fi

exit $pytest_exit
