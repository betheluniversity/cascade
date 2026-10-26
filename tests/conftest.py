import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run-destructive",
        action="store_true",
        default=False,
        help="run tests marked destructive that edit/create content in Cascade",
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "integration: marks tests that require live Cascade access")
    config.addinivalue_line("markers", "destructive: marks tests that modify Cascade content")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-destructive"):
        return

    skip_destructive = pytest.mark.skip(reason="need --run-destructive option to run")
    for item in items:
        if "destructive" in item.keywords:
            item.add_marker(skip_destructive)
