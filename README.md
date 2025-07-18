# Kanboard MCP Server

A Model Context Protocol (MCP) server that exposes Kanboard API functionality to Large Language Models (LLMs), enabling AI assistants to interact with Kanboard project management system.

## Features

This MCP server provides access to 60+ Kanboard API endpoints organized into the following categories:

- **Projects** (5 tools): Get all projects, get project by ID/name, project activity
- **Tasks** (11 tools): Create, read, update, delete tasks; search tasks; handle overdue tasks
- **Categories** (2 tools): Get categories for projects
- **Columns** (2 tools): Get board columns information
- **Boards** (1 tool): Get board information
- **Comments** (5 tools): Create, read, update, delete comments on tasks
- **Users** (9 tools): Get user information, current user data, dashboard, projects
- **Links** (12 tools): Create and manage task links and link types
- **Subtasks** (5 tools): Create, read, update, delete subtasks
- **Tags** (4 tools): Manage task tags
- **Files** (6 tools): Upload, download, and manage task file attachments

## Installation

### Prerequisites

- Python 3.10 or higher
- Access to a Kanboard instance with API enabled
- Kanboard API token

### Install from PyPI (Recommended)

```bash
# Install using uvx (no need to manage Python environments)
uvx kanboard-mcp

# Or install with pip
pip install kanboard-mcp
```

### Install from Source

```bash
# Clone the repository
git clone https://github.com/hoducha/kanboard-mcp.git
cd kanboard-mcp

# Install with uv
uv sync

# Or install with pip
pip install -e .
```

### Development Installation

```bash
# With uv
uv sync --all-extras

# Or with pip
pip install -e ".[dev]"
```

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Required
KANBOARD_URL=https://your-kanboard.com/jsonrpc.php
KANBOARD_API_TOKEN=your_api_token_here

# Optional
KANBOARD_USERNAME=jsonrpc
KANBOARD_VERIFY_SSL=true
KANBOARD_TIMEOUT=30
KANBOARD_MAX_RETRIES=3
KANBOARD_RETRY_DELAY=1.0

# MCP Server settings
MCP_SERVER_NAME="Kanboard MCP Server"
MCP_SERVER_VERSION="0.1.0"
DEBUG=false
```

### Getting Your API Token

1. Log into your Kanboard instance
2. Go to **Settings** → **API**
3. Generate a new API token
4. Copy the token and use it as `KANBOARD_API_TOKEN`

## Usage

### Running the Server

```bash
# Using uvx (recommended - no installation needed)
uvx kanboard-mcp

# Or using the installed command
kanboard-mcp

# Or using Python module
python -m kanboard_mcp.server
```

### MCP Client Integration

Add the server to your MCP client configuration. For Claude Desktop, add to your `claude_desktop_config.json`:

**Option 1: Using uvx (Recommended)**
```json
{
  "mcpServers": {
    "kanboard": {
      "command": "/Users/username/.local/bin/uvx",
      "args": ["kanboard-mcp"],
      "env": {
        "KANBOARD_URL": "https://your-kanboard.com/jsonrpc.php",
        "KANBOARD_API_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

**Note**: Replace `/Users/username/.local/bin/uvx` with your actual uvx path. Find it by running `which uvx` in your terminal.

**Option 2: Using installed package**
```json
{
  "mcpServers": {
    "kanboard": {
      "command": "kanboard-mcp",
      "env": {
        "KANBOARD_URL": "https://your-kanboard.com/jsonrpc.php",
        "KANBOARD_API_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

### Testing the Connection

The server provides built-in tools for testing:

- `test_connection`: Test connection to Kanboard
- `get_server_info`: Get server information and capabilities
- `get_config_info`: Get current configuration (without sensitive data)

## API Tools

### Projects

- `getAllProjects()`: Get all projects
- `getProjectById(project_id)`: Get project by ID
- `getProjectByName(project_name)`: Get project by name
- `getProjectActivity(project_id)`: Get project activity
- `getProjectActivities(project_id)`: Get project activities

### Tasks

- `getAllTasks(project_id, status_id?)`: Get all tasks for a project
- `getTask(task_id)`: Get specific task
- `getTaskByReference(project_id, reference)`: Get task by reference
- `getOverdueTasks()`: Get all overdue tasks
- `getOverdueTasksByProject(project_id)`: Get overdue tasks for project
- `createTask(project_id, title, ...)`: Create new task
- `updateTask(task_id, ...)`: Update existing task
- `openTask(task_id)`: Open task
- `closeTask(task_id)`: Close task
- `removeTask(task_id)`: Delete task
- `searchTasks(project_id, query, ...)`: Search tasks

### Comments

- `createComment(task_id, content, user_id?)`: Create comment
- `getComment(comment_id)`: Get comment
- `getAllComments(task_id)`: Get all comments for task
- `updateComment(comment_id, content)`: Update comment
- `removeComment(comment_id)`: Delete comment

### And many more...

See the individual tool modules in `src/kanboard_mcp/tools/` for complete API documentation.

## Error Handling

All tools return responses in the format:

```json
{
  "success": true,
  "data": { ... }
}
```

Or on error:

```json
{
  "success": false,
  "error": "Error message"
}
```

## Development

### Project Structure

```
kanboard-mcp/
├── src/kanboard_mcp/
│   ├── __init__.py
│   ├── server.py           # Main MCP server
│   ├── config.py           # Configuration management
│   ├── client.py           # Kanboard client wrapper
│   └── tools/              # API tool implementations
│       ├── projects.py
│       ├── tasks.py
│       ├── categories.py
│       ├── columns.py
│       ├── boards.py
│       ├── comments.py
│       ├── users.py
│       ├── links.py
│       ├── subtasks.py
│       ├── tags.py
│       └── files.py
├── pyproject.toml
└── README.md
```

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
black src/

# Sort imports
isort src/

# Type checking
mypy src/

# Linting
ruff src/
```

## Troubleshooting

### Common Issues

1. **Connection Errors**: Check your `KANBOARD_URL` and ensure the API endpoint is correct
2. **Authentication Errors**: Verify your `KANBOARD_API_TOKEN` is valid
3. **SSL Errors**: Set `KANBOARD_VERIFY_SSL=false` for self-signed certificates (not recommended for production)
4. **Timeout Issues**: Increase `KANBOARD_TIMEOUT` value

### Claude Desktop Issues

**Python Command Not Found (`spawn python ENOENT`)**

If you get this error, Claude Desktop can't find the Python executable. Here are the solutions in order of preference:

1. **Use uvx (RECOMMENDED)**:
   ```json
   {
     "mcpServers": {
       "kanboard": {
         "command": "/Users/username/.local/bin/uvx",
         "args": ["kanboard-mcp"],
         "env": { ... }
       }
     }
   }
   ```

2. **Use pip-installed package**:
   ```json
   {
     "mcpServers": {
       "kanboard": {
         "command": "kanboard-mcp",
         "env": { ... }
       }
     }
   }
   ```

3. **Use full Python path**:
   ```json
   {
     "mcpServers": {
       "kanboard": {
         "command": "/usr/local/bin/python3",
         "args": ["-m", "kanboard_mcp.server"],
         "env": {
           "PYTHONPATH": "/path/to/site-packages",
           ...
         }
       }
     }
   }
   ```

**Benefits of uvx**:
- No need to manage Python environments
- Automatically installs and runs the latest version
- Works across different Python installations
- Simplest configuration

### Debug Mode

Enable debug mode for detailed logging:

```bash
DEBUG=true kanboard-mcp
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run code quality checks
6. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Check the troubleshooting section
- Review Kanboard API documentation: https://docs.kanboard.org/v1/api/
- Open an issue on GitHub