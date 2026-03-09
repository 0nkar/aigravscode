# Contributing to Aigravscode

First off, thank you for considering contributing to Aigravscode! 🎉

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, please include as many details as possible using our bug report template.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. Create an issue and provide:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Explain why this enhancement would be useful

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the existing style
6. Issue that pull request!

## Development Setup

We support both Python and Node.js-based development workflows.

### Python Setup
```bash
# Clone and enter the repo
git clone https://github.com/0nkar/aigravscode.git
cd aigravscode

# Create/activate venv and install
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
pip install -e .
pip install pytest black ruff
```

### Node.js Setup
```bash
# Clone and enter the repo
git clone https://github.com/0nkar/aigravscode.git
cd aigravscode

# Install and build (uses npm as a wrapper)
npm install
npm run setup
```

## Style Guidelines

This template is language-agnostic. Follow the appropriate best practices for the language you are contributing in.

### Python Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names (snake_case)
- Add docstrings to functions and classes

### JavaScript / TypeScript Style
- Follow ESLint / Prettier recommended configurations
- Use TypeScript for all new components (camelCase)
- Use descriptive, intentional naming

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Use conventional commits when possible:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `refactor:` for code refactoring
  - `test:` for adding tests

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing! 🚀
