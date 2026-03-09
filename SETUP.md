# Project Setup Guide

This document provides detailed instructions on how to set up `aigravscode` for development.

## Table of Contents
1. [Prerequisites](#1-prerequisites)
2. [Python Development Setup](#2-python-development-setup)
3. [Node.js Tooling Setup](#3-nodejs-tooling-setup)
4. [Environment Variables](#4-environment-variables)
5. [Running Tests](#5-running-tests)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **Node.js & npm** (Optional, for simplified tooling)

---

## 2. Python Development Setup

We recommend using a virtual environment to manage dependencies.

### Step 1: Clone the Repository
```bash
git clone https://github.com/0nkar/aigravscode.git
cd aigravscode
```

### Step 2: Create a Virtual Environment
**On Windows:**
```bash
python -m venv .venv
```
**On macOS/Linux:**
```bash
python3 -m venv .venv
```

### Step 3: Activate the Virtual Environment
**On Windows:**
```bash
.venv\Scripts\activate
```
**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Install the Package in Editable Mode
This allows you to test your changes immediately.
```bash
pip install -e .
```

---

## 3. Node.js Tooling Setup

Even though the core logic is in Python, we provide npm scripts for common tasks.

```bash
npm install
```

### Useful Scripts
- `npm run start`: Runs the main application.
- `npm run test`: Runs the test suite using pytest.
- `npm run setup`: Automates the Python virtual environment setup (Windows only).

---

## 4. Environment Variables

Some features require environment variables. Copy the example file and fill in your values:

```bash
# Example (if .env.example exists)
cp .env.example .env
```
*(Note: Ensure you never commit your `.env` file to version control.)*

---

## 5. Running Tests

We use `pytest` for testing.

**Using Python directly:**
```bash
pytest tests/
```

**Using npm:**
```bash
npm run test
```

---

## 6. Troubleshooting

### Virtual Environment Issues
If you encounter issues with the virtual environment, try deleting the `.venv` folder and starting over.

### Dependency Conflicts
If `pip install` fails, ensure you have the latest version of pip:
```bash
python -m pip install --upgrade pip
```
