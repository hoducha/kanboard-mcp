"""Configuration management for Kanboard MCP Server."""

import os
from typing import Optional

from pydantic import BaseModel, Field, validator


class KanboardConfig(BaseModel):
    """Configuration for Kanboard API connection."""
    
    url: str = Field(..., description="Kanboard API URL (e.g., https://your-kanboard.com/jsonrpc.php)")
    username: str = Field(default="jsonrpc", description="Username for API authentication")
    password: str = Field(..., description="API token or password")
    auth_header: Optional[str] = Field(default=None, description="Custom authentication header")
    verify_ssl: bool = Field(default=True, description="Verify SSL certificates")
    timeout: int = Field(default=30, description="Request timeout in seconds")
    
    @validator('url')
    def validate_url(cls, v: str) -> str:
        """Validate that URL is provided and properly formatted."""
        if not v:
            raise ValueError("Kanboard URL is required")
        
        if not v.startswith(('http://', 'https://')):
            raise ValueError("URL must start with http:// or https://")
        
        if not v.endswith('/jsonrpc.php'):
            if v.endswith('/'):
                v = v + 'jsonrpc.php'
            else:
                v = v + '/jsonrpc.php'
        
        return v
    
    @validator('password')
    def validate_password(cls, v: str) -> str:
        """Validate that API token/password is provided."""
        if not v:
            raise ValueError("API token or password is required")
        return v
    
    @validator('timeout')
    def validate_timeout(cls, v: int) -> int:
        """Validate timeout value."""
        if v <= 0:
            raise ValueError("Timeout must be positive")
        return v


class MCPServerConfig(BaseModel):
    """Configuration for MCP server."""
    
    server_name: str = Field(default="Kanboard MCP Server", description="Name of the MCP server")
    server_version: str = Field(default="0.1.0", description="Version of the MCP server")
    debug: bool = Field(default=False, description="Enable debug mode")
    max_retries: int = Field(default=3, description="Maximum number of API retries")
    retry_delay: float = Field(default=1.0, description="Delay between retries in seconds")
    
    @validator('max_retries')
    def validate_max_retries(cls, v: int) -> int:
        """Validate max retries value."""
        if v < 0:
            raise ValueError("Max retries must be non-negative")
        return v
    
    @validator('retry_delay')
    def validate_retry_delay(cls, v: float) -> float:
        """Validate retry delay value."""
        if v < 0:
            raise ValueError("Retry delay must be non-negative")
        return v


class Config(BaseModel):
    """Main configuration class."""
    
    kanboard: KanboardConfig
    server: MCPServerConfig = Field(default_factory=MCPServerConfig)
    
    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables."""
        kanboard_config = KanboardConfig(
            url=os.getenv("KANBOARD_URL", ""),
            username=os.getenv("KANBOARD_USERNAME", "jsonrpc"),
            password=os.getenv("KANBOARD_API_TOKEN", ""),
            auth_header=os.getenv("KANBOARD_AUTH_HEADER"),
            verify_ssl=os.getenv("KANBOARD_VERIFY_SSL", "true").lower() == "true",
            timeout=int(os.getenv("KANBOARD_TIMEOUT", "30")),
        )
        
        server_config = MCPServerConfig(
            server_name=os.getenv("MCP_SERVER_NAME", "Kanboard MCP Server"),
            server_version=os.getenv("MCP_SERVER_VERSION", "0.1.0"),
            debug=os.getenv("DEBUG", "false").lower() == "true",
            max_retries=int(os.getenv("KANBOARD_MAX_RETRIES", "3")),
            retry_delay=float(os.getenv("KANBOARD_RETRY_DELAY", "1.0")),
        )
        
        return cls(kanboard=kanboard_config, server=server_config)
    
    def validate_config(self) -> None:
        """Validate the complete configuration."""
        if not self.kanboard.url:
            raise ValueError("KANBOARD_URL environment variable is required")
        
        if not self.kanboard.password:
            raise ValueError("KANBOARD_API_TOKEN environment variable is required")


def load_config() -> Config:
    """Load and validate configuration from environment variables."""
    try:
        config = Config.from_env()
        config.validate_config()
        return config
    except Exception as e:
        raise ValueError(f"Configuration error: {str(e)}")


def get_example_env() -> str:
    """Get example environment variables configuration."""
    return """
# Kanboard MCP Server Configuration
# Required environment variables:

# Kanboard API URL (required)
KANBOARD_URL=https://your-kanboard.com/jsonrpc.php

# Kanboard API Token (required)
KANBOARD_API_TOKEN=your_api_token_here

# Optional configuration:
KANBOARD_USERNAME=jsonrpc
KANBOARD_VERIFY_SSL=true
KANBOARD_TIMEOUT=30
KANBOARD_MAX_RETRIES=3
KANBOARD_RETRY_DELAY=1.0

# MCP Server settings:
MCP_SERVER_NAME="Kanboard MCP Server"
MCP_SERVER_VERSION="0.1.0"
DEBUG=false
""".strip()