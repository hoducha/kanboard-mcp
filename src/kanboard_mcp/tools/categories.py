"""Category-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register category-related tools."""
    
    @mcp.tool()
    def getCategory(category_id: int) -> Dict[str, Any]:
        """Get a specific category by ID.
        
        Args:
            category_id: The ID of the category to retrieve
        """
        try:
            category = client.call_api("get_category", category_id)
            return {
                "success": True,
                "data": category
            }
        except KanboardClientError as e:
            logger.error(f"Error getting category {category_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getAllCategories(project_id: int) -> Dict[str, Any]:
        """Get all categories for a project.
        
        Args:
            project_id: The ID of the project to get categories for
        """
        try:
            categories = client.call_api("get_all_categories", project_id)
            return {
                "success": True,
                "data": categories,
                "count": len(categories) if categories else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting all categories for project {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }