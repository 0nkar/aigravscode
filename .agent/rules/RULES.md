---
trigger: model_decision
---

# Agent Rules — aigravscode

## Project Context

**aigravscode** is a multi-stack starter template. Source files in `src/aigravscode/` are intentional stubs — do not implement them unless explicitly asked.

## Project Structure

```
aigravscode/
├── .agent/              # AI config (rules, skills, memory)
├── .github/             # CI/CD and GitHub templates
├── src/aigravscode/     # Python package (stubs)
├── tests/               # Pytest suite
├── pyproject.toml       # Python config + tool settings
├── package.json         # npm tooling wrapper
├── requirements.txt     # Runtime dependencies
└── .env.example         # Environment variable template
```

## Commands

| Task | Command |
|------|---------|
| Install | `pip install -e ".[dev]"` |
| Run | `python -m aigravscode.main` |
| Test | `pytest tests/` |
| Lint | `ruff check src/` |
| Format | `black src/ tests/` |

## Python Standards

- Follow PEP 8 strictly
- Type hints on all function parameters and return values
- Max line length: 88 (Black-compatible)
- Docstrings on all public modules, classes, and functions
- Use f-strings — not `.format()` or `%`
- Use `logging` — not `print()`
- Keep functions under 50 lines
- Group imports: stdlib → third-party → local

## JavaScript / TypeScript Standards

- ESLint / Prettier recommended config
- TypeScript for all new logic
- ES modules (`import`/`export`)
- JSDoc for complex non-obvious functions

## Naming Conventions

| Context | Convention |
|---------|-----------|
| Python functions / variables | `snake_case` |
| Python classes | `PascalCase` |
| JS/TS functions / variables | `camelCase` |
| JS/TS classes | `PascalCase` |

## Git Commits

Use conventional commits:

- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation only
- `refactor:` — no behavior change
- `test:` — tests only
- `chore:` — maintenance (deps, CI, config)

## Rules

1. Never hardcode config or secrets — use environment variables (see `.env.example`)
2. Never commit `.env`
3. Write tests for new functionality
4. Update relevant docs when behavior changes
5. Ask before making breaking changes to core structure
6. Prefer absolute imports over relative imports
