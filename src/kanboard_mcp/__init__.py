"""Kanboard MCP Server - Model Context Protocol server for Kanboard API."""

__version__ = "0.1.0"
__author__ = "Kanboard MCP Contributors"
__email__ = "contributors@example.com"

from .server import create_server

__all__ = ["create_server"]