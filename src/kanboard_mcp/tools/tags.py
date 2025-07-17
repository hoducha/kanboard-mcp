"""Tag-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register tag-related tools."""
    
    @mcp.tool()
    def getAllTags() -> Dict[str, Any]:
        """Get all available tags."""
        try:
            tags = client.call_api("get_all_tags")
            return {
                "success": True,
                "data": tags,
                "count": len(tags) if tags else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting all tags: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getTagsByProject(project_id: int) -> Dict[str, Any]:
        """Get all tags for a specific project.
        
        Args:
            project_id: The ID of the project to get tags for
        """
        try:
            tags = client.call_api("get_tags_by_project", project_id)
            return {
                "success": True,
                "data": tags,
                "count": len(tags) if tags else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting tags for project {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def setTaskTags(task_id: int, tags: List[str]) -> Dict[str, Any]:
        """Set tags for a task.
        
        Args:
            task_id: The ID of the task to set tags for
            tags: List of tag names to assign to the task
        """
        try:
            success = client.call_api("set_task_tags", task_id, tags)
            return {
                "success": True,
                "data": {"updated": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error setting tags for task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getTaskTags(task_id: int) -> Dict[str, Any]:
        """Get tags for a specific task.
        
        Args:
            task_id: The ID of the task to get tags for
        """
        try:
            tags = client.call_api("get_task_tags", task_id)
            return {
                "success": True,
                "data": tags,
                "count": len(tags) if tags else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting tags for task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }