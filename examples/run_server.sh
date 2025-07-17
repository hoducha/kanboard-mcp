#!/bin/bash

# Kanboard MCP Server Wrapper Script
# This script ensures the server runs with the correct Python environment

# IMPORTANT: Update these paths to match your system
# Set up environment
export PATH="/path/to/your/python/bin:$PATH"
export PYTHONPATH="/path/to/kanboard-mcp/src:$PYTHONPATH"

# Change to the project directory
cd "/path/to/kanboard-mcp"

# Run the server
exec "/path/to/your/python/bin/python" -m kanboard_mcp.server