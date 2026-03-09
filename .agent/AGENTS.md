# AGENTS.md

Project context for AI agents working on this codebase.

## What This Project Is

**aigravscode** is a multi-stack project starter template. The stubs in `src/aigravscode/` are intentional — they define the structure that developers build on top of. Do not fill in stub implementations unless asked.

## Tech Stack

- **Primary language**: Python 3.8+
- **Dev tools**: ruff (lint), black (format), pytest + pytest-cov (test)
- **Runtime deps**: `python-dotenv`, `requests`
- **Node.js**: tooling wrapper only (`package.json` npm scripts)
- **CI**: GitHub Actions (`.github/workflows/python-ci.yml`)

## Commands

```bash
pip install -e ".[dev]"     # install with dev dependencies
python -m aigravscode.main  # run
pytest tests/               # test
ruff check src/             # lint
black src/ tests/           # format
```

## Code Conventions

- **Python**: PEP 8, type hints on all functions, max 88 chars (Black), f-strings preferred
- **JS/TS**: ESLint/Prettier, TypeScript preferred, ES modules
- **Naming**: `snake_case` functions/vars (Python), `camelCase` (JS/TS), `PascalCase` classes (both)
- **Commits**: conventional commits — `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
- Never hardcode secrets — use `.env` (see `.env.example`)
- No `print()` debugging — use `logging`

## Directory Layout

```
src/aigravscode/   Main Python package (stubs)
tests/             Pytest test suite
.agent/            AI agent config (rules, skills, memory)
.github/workflows/ CI/CD
```

## Rules

- Match the language and style already present in the file you're editing
- Add type hints and docstrings to all new Python functions/classes
- Keep functions under 50 lines; split if longer
- Add or update tests when adding functionality
- Update docs when changing behavior
