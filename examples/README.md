# Examples

This directory contains example configurations and scripts for using the Kanboard MCP Server.

## Files

### Claude Desktop Configuration Examples

- **`claude_desktop_config.json.example`** - Simple configuration example
- **`claude_desktop_config_options.json`** - Multiple configuration options for different setups

### Scripts

- **`run_server.sh`** - Bash wrapper script for running the server with proper environment setup

## Usage

### Claude Desktop Setup

1. **Choose your configuration method** from the options in `claude_desktop_config_options.json`
2. **Copy the relevant configuration** to your Claude Desktop config file
3. **Update the paths** to match your system:
   - Replace `/path/to/your/python/bin/` with your actual Python installation path
   - Replace `/path/to/kanboard-mcp/` with your actual project path
   - Replace placeholder URLs and tokens with your actual Kanboard credentials

### Finding Your Python Path

Run one of these commands to find your Python installation:

```bash
# For system Python
which python3

# For pyenv users
which python

# For conda users
conda info --envs
```

Common Python paths:
- System Python: `/usr/local/bin/python3` or `/usr/bin/python3`
- pyenv: `~/.pyenv/versions/X.X.X/bin/python`
- conda: `~/anaconda3/bin/python` or `~/miniconda3/bin/python`

### Wrapper Script Setup

1. **Copy the script** to your desired location
2. **Update the paths** in `run_server.sh`:
   ```bash
   export PATH="/your/python/bin:$PATH"
   export PYTHONPATH="/your/kanboard-mcp/src:$PYTHONPATH"
   cd "/your/kanboard-mcp"
   exec "/your/python/bin/python" -m kanboard_mcp.server
   ```
3. **Make it executable**:
   ```bash
   chmod +x run_server.sh
   ```

### Environment Variables

All configuration examples support these environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `KANBOARD_URL` | Your Kanboard API endpoint | `https://your-kanboard.com/jsonrpc.php` |
| `KANBOARD_API_TOKEN` | Your Kanboard API token | `your_api_token_here` |
| `KANBOARD_USERNAME` | Your Kanboard username | `your_username` |
| `KANBOARD_VERIFY_SSL` | SSL certificate verification | `true` or `false` |
| `DEBUG` | Enable debug logging | `true` or `false` |

## Troubleshooting

### Common Issues

1. **Python not found**: Update the `command` path in your configuration
2. **Module not found**: Ensure `PYTHONPATH` includes the `src` directory
3. **Permission denied**: Make sure the script is executable (`chmod +x`)
4. **Connection errors**: Verify your Kanboard URL and API token

### Getting Help

If you encounter issues:
1. Check the main README troubleshooting section
2. Verify your paths and credentials
3. Test the server manually: `python -m kanboard_mcp.server`
4. Check Claude Desktop logs for specific error messages