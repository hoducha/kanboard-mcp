# Contributing to Kanboard MCP Server

Thank you for your interest in contributing to the Kanboard MCP Server! This document provides guidelines for contributing to the project.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Access to a Kanboard instance for testing
- Git for version control

### Setting up the Development Environment

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/hoducha/kanboard-mcp.git
   cd kanboard-mcp
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Set up your environment**
   ```bash
   cp .env.example .env
   # Edit .env with your Kanboard credentials
   ```

## Development Workflow

### Code Style

This project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **mypy**: Type checking
- **ruff**: Linting

Run all checks before submitting:
```bash
black src/
isort src/
mypy src/
ruff src/
```

### Testing

1. **Run the server locally**
   ```bash
   python -m kanboard_mcp.server
   ```

2. **Test with Claude Desktop**
   - Configure Claude Desktop with your local server
   - Test various API calls to ensure functionality

### Project Structure

```
kanboard-mcp/
├── src/kanboard_mcp/
│   ├── __init__.py          # Package initialization
│   ├── server.py            # Main MCP server implementation
│   ├── config.py            # Configuration management
│   ├── client.py            # Kanboard API client wrapper
│   └── tools/               # API tool implementations
│       ├── __init__.py
│       ├── projects.py      # Project-related tools
│       ├── tasks.py         # Task management tools
│       ├── categories.py    # Category tools
│       ├── columns.py       # Column tools
│       ├── boards.py        # Board tools
│       ├── comments.py      # Comment tools
│       ├── users.py         # User management tools
│       ├── links.py         # Task linking tools
│       ├── subtasks.py      # Subtask tools
│       ├── tags.py          # Tag tools
│       └── files.py         # File management tools
├── examples/                # Configuration examples
├── pyproject.toml           # Project configuration
├── README.md                # Main documentation
├── CHANGELOG.md             # Version history
└── CONTRIBUTING.md          # This file
```

## Contributing Guidelines

### Adding New Tools

1. **Choose the appropriate module** in `src/kanboard_mcp/tools/`
2. **Follow the existing pattern**:
   ```python
   @mcp.tool()
   def your_tool_name(param1: int, param2: str) -> Dict[str, Any]:
       """Tool description.
       
       Args:
           param1: Description of param1
           param2: Description of param2
       """
       try:
           result = client.call_api("kanboard_api_method", param1, param2)
           return {
               "success": True,
               "data": result
           }
       except KanboardClientError as e:
           logger.error(f"Error in your_tool_name: {e}")
           return {
               "success": False,
               "error": str(e)
           }
   ```

3. **Add proper type hints** for all parameters and return values
4. **Include comprehensive docstrings** with parameter descriptions
5. **Handle errors gracefully** with appropriate error messages
6. **Update the README** with your new tool information

### Submitting Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards
3. **Test thoroughly** with a real Kanboard instance
4. **Update documentation** if needed
5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request** with:
   - Clear description of changes
   - Testing instructions
   - Any breaking changes noted

### Commit Message Format

Use conventional commits format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for code style changes
- `refactor:` for code refactoring
- `test:` for test-related changes
- `chore:` for maintenance tasks

Examples:
- `feat: add support for project archiving`
- `fix: handle connection timeout errors properly`
- `docs: update Claude Desktop configuration instructions`

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment include:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated promptly and fairly.

## Questions?

If you have questions about contributing, please:
1. Check the existing issues and discussions
2. Create a new issue with the "question" label
3. Provide as much context as possible

Thank you for contributing to Kanboard MCP Server!