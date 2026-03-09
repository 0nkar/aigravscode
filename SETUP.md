# Setup Guide

## Prerequisites

- Python 3.8+
- pip
- Node.js & npm (optional — for the npm tooling wrapper)

## Python Setup

```bash
# 1. Clone
git clone https://github.com/0nkar/aigravscode.git
cd aigravscode

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install the package and dev dependencies
pip install -e ".[dev]"
```

## Node.js Setup (optional)

```bash
npm install
```

Useful npm scripts:

| Script | Command | Description |
|--------|---------|-------------|
| `npm run start` | `python -m aigravscode.main` | Run the application |
| `npm test` | `python -m pytest tests/` | Run the test suite |
| `npm run lint` | `ruff check src/` | Lint source files |
| `npm run setup` | full install | Set up venv and install dependencies |

## Environment Variables

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

Never commit `.env` to version control.

## Running Tests

```bash
pytest tests/
```

## Running Linting

```bash
ruff check src/
black --check src/
```

## Troubleshooting

**Virtual environment issues** — delete `.venv` and start over:
```bash
rm -rf .venv
python -m venv .venv
```

**Outdated pip** — upgrade before installing:
```bash
python -m pip install --upgrade pip
```

**Import errors** — ensure the package is installed in editable mode:
```bash
pip install -e ".[dev]"
```
