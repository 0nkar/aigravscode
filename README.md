# aigravscode

A multi-stack project starter template with integrated Antigravity AI configuration.

[![Python CI](https://github.com/0nkar/aigravscode/actions/workflows/python-ci.yml/badge.svg)](https://github.com/0nkar/aigravscode/actions/workflows/python-ci.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **For AI agents / LLMs** — see [`.agent/AGENTS.md`](.agent/AGENTS.md) for project context and development workflows.  
> **For developers** — see [`SETUP.md`](SETUP.md) for environment setup instructions.

## Features

- **Language-agnostic** — pre-configured for Python; ready to extend with Node.js, Go, TypeScript, etc.
- **AI-ready** — built-in `.agent/` configuration for Antigravity AI workflows and agent skills
- **Consistent tooling** — npm scripts wrap Python commands for a unified cross-stack experience
- **CI/CD included** — GitHub Actions workflow with linting, testing, and build steps out of the box

## Quick Start

```bash
git clone https://github.com/0nkar/aigravscode.git
cd aigravscode

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -e ".[dev]"
```

## Usage

```bash
# Run
python -m aigravscode.main

# Test
pytest tests/

# Lint
ruff check src/
```

Or use the npm wrapper:

```bash
npm run start
npm test
npm run lint
```

## Project Structure

```
aigravscode/
├── .agent/                  # AI agent configuration
│   ├── rules/RULES.md       # Coding standards and behavior rules
│   ├── skills/SKILL.md      # Custom agent skill template
│   ├── AGENTS.md            # Project context for AI agents
│   └── MEMORY.md            # Long-term project memory
├── .github/
│   ├── workflows/           # GitHub Actions CI/CD
│   └── ISSUE_TEMPLATE/      # Bug and feature request templates
├── src/aigravscode/         # Main Python package (stubs — fill in as needed)
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── agent.py             # Agent logic
│   ├── config.py            # Environment-based configuration
│   ├── llm.py               # LLM provider integration
│   └── utils.py             # Utility functions
├── tests/                   # Pytest test suite
├── .env.example             # Environment variable template
├── pyproject.toml           # Python package config, linting, and test settings
├── requirements.txt         # Runtime dependencies
├── package.json             # npm tooling wrapper
├── CONTRIBUTING.md          # Contribution guidelines
├── SETUP.md                 # Detailed setup guide
└── LICENSE                  # MIT License
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Bug reports and feature requests go through [GitHub Issues](https://github.com/0nkar/aigravscode/issues).

## License

MIT — see [LICENSE](LICENSE).
