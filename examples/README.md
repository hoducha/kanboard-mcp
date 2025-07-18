# Examples

This directory contains example configurations for using the Kanboard MCP Server.

## Files

### Claude Desktop Configuration Examples

- **`claude_desktop_config_options.json`** - Multiple configuration options for different setups

## Usage

### Claude Desktop Setup

1. **Choose your configuration method** from the options in `claude_desktop_config_options.json`
2. **Copy the relevant configuration** to your Claude Desktop config file
3. **Update the configuration** with your system paths and Kanboard credentials:
   - Replace `/Users/username/.local/bin/uvx` with your actual uvx path (run `which uvx` to find it)
   - Replace `https://your-kanboard.com/jsonrpc.php` with your actual Kanboard URL
   - Replace `your_api_token_here` with your actual API token
   - Replace `your_username` with your actual username

### Configuration Options

**Option 1: Using uvx (Recommended)**
- No installation required
- Automatically manages Python environments
- Always uses the latest published version
- Simplest configuration

**Option 2: Using uvx with local development version**
- For developers working on the codebase
- Runs from local source code
- Update `/path/to/kanboard-mcp` to your project directory

**Option 3: Using pip-installed package**
- Traditional installation method
- Requires `pip install kanboard-mcp`
- Good for environments where uvx isn't available

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

1. **uvx not found (`spawn uvx ENOENT`)**: 
   - Find uvx path: `which uvx` (usually `/Users/username/.local/bin/uvx`)
   - Use full path in config: `"command": "/Users/username/.local/bin/uvx"`
   - Or install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. **Connection errors**: Verify your Kanboard URL and API token
3. **Permission errors**: Check that your API token has sufficient permissions
4. **SSL errors**: Set `KANBOARD_VERIFY_SSL=false` for self-signed certificates

### Getting Help

If you encounter issues:
1. Check the main README troubleshooting section
2. Verify your Kanboard credentials
3. Test the server manually: `uvx kanboard-mcp` or `kanboard-mcp`
4. Check Claude Desktop logs for specific error messages