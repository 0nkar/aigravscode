# Contributing

## Getting Started

1. Fork the repository and clone your fork
2. Set up your environment — see [SETUP.md](SETUP.md)
3. Create a feature branch: `git checkout -b feat/my-change`
4. Make your changes
5. Run tests and linting before committing
6. Open a pull request against `main`

## Development Commands

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Lint
ruff check src/

# Format
black src/ tests/
```

## Commit Style

Use [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | When to use |
|--------|-------------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `refactor:` | Code change with no behavior change |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance (deps, config, CI) |

Example: `feat: add retry logic to LLM provider`

## Code Standards

**Python**
- Follow PEP 8; max line length 88 (Black-compatible)
- Use type hints on all function signatures
- No `print()` for debugging — use `logging`
- Keep functions under 50 lines

**JavaScript / TypeScript**
- Follow ESLint / Prettier recommended config
- Prefer TypeScript over plain JavaScript
- Use ES modules (`import`/`export`)

**All languages**
- No hardcoded secrets or config values — use environment variables
- Add tests for new functionality
- Update docs when changing behavior

## Reporting Issues

- Search existing issues before opening a new one
- Use the bug report or feature request templates
- For security issues, see [SECURITY.md](.github/SECURITY.md) — do not open a public issue

## Pull Request Checklist

- Tests pass (`pytest tests/`)
- Linting passes (`ruff check src/`)
- Documentation updated if behavior changed
- PR description explains what and why
