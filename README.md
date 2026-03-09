# Project Starter Template

[![Python CI](https://github.com/0nkar/aigravscode/actions/workflows/python-ci.yml/badge.svg)](https://github.com/0nkar/aigravscode/actions/workflows/python-ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A modern, multi-stack project starter template with integrated Antigravity AI configuration.
> 
> [!IMPORTANT]
> **For AI Agents/LLMs**: Please refer to [.agent/AGENTS.md](.agent/AGENTS.md) for project context, architecture, and development workflows. This project uses `AGENTS.md` instead of `CLAUDE.md`.
>
> **For Developers**: Please see [SETUP.md](SETUP.md) for detailed installation and environment configuration instructions. For security reporting, refer to [SECURITY.md](SECURITY.md).

## 🚀 Features

- **Multi-Stack Ready**: Pre-configured for Python and Node.js environments.
- **AI-Enhanced**: Built-in Antigravity agent configuration for streamlined development.
- **Consistent Tooling**: Unified workflow using NPM scripts even for Python tasks.
- **CI/CD Integrated**: Ready-to-use GitHub Actions workflows.

## 📦 Installation

### Prerequisites

#### Core (Current implementation)
- Python 3.8+ and `pip`

#### Optional (Other stacks supported)
- Node.js & npm (for JavaScript/TypeScript)
- Go, Rust, or any other appropriate tooling for your stack

### Quick Start

```bash
# Setup virtual environment and install dependencies
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
pip install -e .
```

For more detailed instructions, please refer to the [Setup Guide](SETUP.md).

## 🎯 Usage

### Python (Current Core)
```bash
# Run the application
python -m aigravscode.main
```

### Node.js (Tooling Wrapper)
```bash
# Or using the npm wrapper
npm run start
```

## 📁 Project Structure

```
aigravscode/
├── docs/                   # Documentation files
├── examples/               # Example usage scripts
├── .github/                # GitHub-specific configurations
│   ├── workflows/          # GitHub Actions CI/CD
│   └── ISSUE_TEMPLATE/     # Issue templates
├── .agent/                 # Antigravity agent configuration
│   ├── skills/             # Custom AI capabilities
│   ├── workflows/          # Automated multi-step procedures
│   └── AGENTS.md           # AI assistant context & instructions
├── src/                    # Source code directory
│   └── aigravscode/          # Main Python package
│       ├── __init__.py
│       ├── main.py          # Application entry point
│       ├── agent.py         # Agent logic
│       ├── config.py        # Configuration management
│       ├── llm.py           # LLM provider integration
│       └── utils.py         # Utility functions
├── package.json            # Node.js project configuration (tooling wrapper)
├── CONTRIBUTING.md         # Contribution guidelines
├── LICENSE                 # MIT License
├── pyproject.toml          # Project configuration
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Antigravity AI](https://github.com/antigravity) capabilities
- Inspired by modern agentic coding practices

---

<p align="center">
  Made with ❤️ by the Aigravscode Team
</p>
