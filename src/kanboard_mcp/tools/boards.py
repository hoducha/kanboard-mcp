"""Board-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register board-related tools."""
    
    @mcp.tool()
    def getBoard(project_id: int) -> Dict[str, Any]:
        """Get board information for a project.
        
        Args:
            project_id: The ID of the project to get board for
        """
        try:
            board = client.call_api("get_board", project_id)
            return {
                "success": True,
                "data": board
            }
        except KanboardClientError as e:
            logger.error(f"Error getting board for project {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }