# bu-cascade

Python package for integrating with Cascade Server web services.

## Project layout

This package follows the PyPA packaging tutorial layout:

```
cascade/
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── src/
│   └── bu_cascade/
└── tests/
```

## Dependencies

- suds-community
- beautifulsoup4

## Build distributions

From the project directory:

```bash
python3 -m pip install --upgrade pip build
python3 -m build
```

This creates source and wheel distributions in `dist/`.

## Upload to TestPyPI

```bash
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

## Install from TestPyPI

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps bu-cascade
```
