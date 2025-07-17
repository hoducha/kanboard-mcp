"""Main MCP server implementation for Kanboard API."""

import asyncio
import logging
import sys
from typing import Any, Dict, List, Optional, Union

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

from .config import Config, load_config
from .client import KanboardClient, create_client, KanboardClientError
from .tools import (
    projects,
    tasks,
    categories,
    columns,
    boards,
    comments,
    users,
    links,
    subtasks,
    tags,
    files,
)


# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class KanboardMCPServer:
    """Kanboard MCP Server implementation."""
    
    def __init__(self, config: Config):
        """Initialize the MCP server with configuration."""
        self.config = config
        self.client = create_client(config)
        self.mcp = FastMCP(config.server.server_name)
        
        # Set up logging level
        if config.server.debug:
            logging.getLogger().setLevel(logging.DEBUG)
            logger.debug("Debug mode enabled")
        
        # Register tools
        self._register_tools()
        
        # Add connection test tool
        self._register_connection_tools()
    
    def _register_tools(self) -> None:
        """Register all Kanboard API tools."""
        tool_modules = [
            projects,
            tasks,
            categories,
            columns,
            boards,
            comments,
            users,
            links,
            subtasks,
            tags,
            files,
        ]
        
        for module in tool_modules:
            if hasattr(module, 'register_tools'):
                module.register_tools(self.mcp, self.client)
                logger.info(f"Registered tools from {module.__name__}")
    
    def _register_connection_tools(self) -> None:
        """Register connection and server management tools."""
        
        @self.mcp.tool()
        def test_connection() -> Dict[str, Any]:
            """Test connection to Kanboard server and return status."""
            try:
                result = self.client.test_connection()
                return {
                    "success": True,
                    "data": result
                }
            except Exception as e:
                logger.error(f"Connection test failed: {e}")
                return {
                    "success": False,
                    "error": str(e)
                }
        
        @self.mcp.tool()
        def get_server_info() -> Dict[str, Any]:
            """Get Kanboard server information and capabilities."""
            try:
                result = self.client.get_server_info()
                return {
                    "success": True,
                    "data": result
                }
            except Exception as e:
                logger.error(f"Failed to get server info: {e}")
                return {
                    "success": False,
                    "error": str(e)
                }
        
        @self.mcp.tool()
        def get_config_info() -> Dict[str, Any]:
            """Get current configuration information (without sensitive data)."""
            return {
                "success": True,
                "data": {
                    "server_name": self.config.server.server_name,
                    "server_version": self.config.server.server_version,
                    "debug": self.config.server.debug,
                    "max_retries": self.config.server.max_retries,
                    "retry_delay": self.config.server.retry_delay,
                    "kanboard_url": self.config.kanboard.url,
                    "kanboard_username": self.config.kanboard.username,
                    "verify_ssl": self.config.kanboard.verify_ssl,
                    "timeout": self.config.kanboard.timeout,
                }
            }
    
    def run(self) -> None:
        """Run the MCP server."""
        try:
            logger.info(f"Starting {self.config.server.server_name} v{self.config.server.server_version}")
            logger.info(f"Connecting to Kanboard at {self.config.kanboard.url}")
            
            # Test connection on startup
            connection_result = self.client.test_connection()
            if connection_result.get("connected"):
                logger.info("Successfully connected to Kanboard")
            else:
                logger.error(f"Failed to connect to Kanboard: {connection_result.get('error')}")
                raise ConnectionError(f"Cannot connect to Kanboard: {connection_result.get('error')}")
            
            # Run the server
            self.mcp.run()
            
        except KeyboardInterrupt:
            logger.info("Server stopped by user")
        except Exception as e:
            logger.error(f"Server error: {e}")
            raise


def create_server(config: Optional[Config] = None) -> KanboardMCPServer:
    """Create a new Kanboard MCP server instance."""
    if config is None:
        config = load_config()
    
    return KanboardMCPServer(config)


def main() -> None:
    """Main entry point for the MCP server."""
    try:
        # Load configuration
        config = load_config()
        
        # Create and run server
        server = create_server(config)
        server.run()
        
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        print(f"Configuration error: {e}", file=sys.stderr)
        print("Please check your environment variables.", file=sys.stderr)
        sys.exit(1)
    except ConnectionError as e:
        logger.error(f"Connection error: {e}")
        print(f"Connection error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()