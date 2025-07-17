"""Column-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register column-related tools."""
    
    @mcp.tool()
    def getColumns(project_id: int) -> Dict[str, Any]:
        """Get all columns for a project.
        
        Args:
            project_id: The ID of the project to get columns for
        """
        try:
            columns = client.call_api("get_columns", project_id)
            return {
                "success": True,
                "data": columns,
                "count": len(columns) if columns else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting columns for project {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getColumn(column_id: int) -> Dict[str, Any]:
        """Get a specific column by ID.
        
        Args:
            column_id: The ID of the column to retrieve
        """
        try:
            column = client.call_api("get_column", column_id)
            return {
                "success": True,
                "data": column
            }
        except KanboardClientError as e:
            logger.error(f"Error getting column {column_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }