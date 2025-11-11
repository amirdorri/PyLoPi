# Contributing to PyLoPi

First off, thank you for considering contributing to PyLoPi! It's people like you that make PyLoPi such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include screenshots if possible
* Include your environment details (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* Use a clear and descriptive title
* Provide a step-by-step description of the suggested enhancement
* Provide specific examples to demonstrate the steps
* Describe the current behavior and explain which behavior you expected to see instead
* Explain why this enhancement would be useful

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Include screenshots and animated GIFs in your pull request whenever possible
* Follow the Python style guide (PEP 8)
* Include thoughtfully-worded, well-structured tests
* Document new code
* End all files with a newline

## Development Setup

1. Fork the repo
2. Clone your fork
```bash
git clone https://github.com/PicoBaz/PyLoPi.git
cd PyLoPi
```

3. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Create a branch
```bash
git checkout -b feature/your-feature-name
```

## Coding Standards

### Python Style Guide

* Follow PEP 8
* Use 4 spaces for indentation
* Maximum line length of 100 characters
* Use descriptive variable names
* Add docstrings to all functions and classes

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Example:
```
Add support for MySQL log parsing

- Implement MySQL error pattern matching
- Add MySQL-specific error analysis
- Update documentation with MySQL examples

Closes #123
```

## Testing

Before submitting a pull request, please ensure:

* All existing tests pass
* New features include appropriate tests
* Code coverage remains high

Run tests with:
```bash
python -m pytest tests/
```

## Documentation

* Update the README.md with details of changes to the interface
* Update the documentation for any new features
* Add comments in code for complex logic
* Include docstrings for all public methods

## Project Structure

Understanding the project structure will help you contribute more effectively:

```
PyLoPi/
├── app.py              # Main application entry point
├── database.py         # Database operations
├── log_analyzer.py     # Core analysis logic
├── email_notifier.py   # Email functionality
├── config_manager.py   # Configuration handling
├── templates/          # HTML templates
│   └── index.html     # Main web interface
└── tests/             # Test files
```

## Adding New Features

### Adding a New Error Type

1. Edit `log_analyzer.py`
2. Add pattern to `error_patterns` dictionary
3. Add analysis in `generate_analysis()`
4. Add solution in `get_default_solution()`
5. Add code fix in `generate_code_fix()`
6. Update tests
7. Update documentation

### Adding a New Language

1. Edit `templates/index.html`
2. Add translations to `translations` object
3. Test language switching
4. Update README

### Adding a New Plugin

1. Create new file in project root
2. Import in `app.py`
3. Add initialization code
4. Add API endpoints if needed
5. Update configuration
6. Add documentation

## Release Process

1. Update version number in `setup.py`
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Push to GitHub
6. Create GitHub release

## Community

* Join our discussions on GitHub
* Follow development updates
* Help others in issues and discussions

## Questions?

Feel free to open an issue with your question or reach out to the maintainers directly.

Thank you for contributing to PyLoPi! 🎉