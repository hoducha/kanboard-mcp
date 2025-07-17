"""Subtask-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register subtask-related tools."""
    
    @mcp.tool()
    def createSubtask(task_id: int, title: str, user_id: Optional[int] = None, time_estimated: Optional[int] = None, time_spent: Optional[int] = None, status: Optional[int] = None) -> Dict[str, Any]:
        """Create a new subtask.
        
        Args:
            task_id: The ID of the parent task
            title: The title of the subtask
            user_id: The ID of the user assigned to the subtask
            time_estimated: Estimated time in hours
            time_spent: Time spent in hours
            status: Status of the subtask (0=todo, 1=in progress, 2=done)
        """
        try:
            subtask_data = {
                "task_id": task_id,
                "title": title
            }
            
            if user_id is not None:
                subtask_data["user_id"] = user_id
            if time_estimated is not None:
                subtask_data["time_estimated"] = time_estimated
            if time_spent is not None:
                subtask_data["time_spent"] = time_spent
            if status is not None:
                subtask_data["status"] = status
            
            subtask_id = client.call_api("create_subtask", **subtask_data)
            return {
                "success": True,
                "data": {"subtask_id": subtask_id}
            }
        except KanboardClientError as e:
            logger.error(f"Error creating subtask: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getSubtask(subtask_id: int) -> Dict[str, Any]:
        """Get a specific subtask by ID.
        
        Args:
            subtask_id: The ID of the subtask to retrieve
        """
        try:
            subtask = client.call_api("get_subtask", subtask_id)
            return {
                "success": True,
                "data": subtask
            }
        except KanboardClientError as e:
            logger.error(f"Error getting subtask {subtask_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getAllSubtasks(task_id: int) -> Dict[str, Any]:
        """Get all subtasks for a task.
        
        Args:
            task_id: The ID of the task to get subtasks for
        """
        try:
            subtasks = client.call_api("get_all_subtasks", task_id)
            return {
                "success": True,
                "data": subtasks,
                "count": len(subtasks) if subtasks else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting all subtasks for task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def updateSubtask(subtask_id: int, title: Optional[str] = None, user_id: Optional[int] = None, time_estimated: Optional[int] = None, time_spent: Optional[int] = None, status: Optional[int] = None) -> Dict[str, Any]:
        """Update an existing subtask.
        
        Args:
            subtask_id: The ID of the subtask to update
            title: The new title of the subtask
            user_id: The new user ID assigned to the subtask
            time_estimated: New estimated time in hours
            time_spent: New time spent in hours
            status: New status of the subtask (0=todo, 1=in progress, 2=done)
        """
        try:
            subtask_data = {"id": subtask_id}
            
            if title is not None:
                subtask_data["title"] = title
            if user_id is not None:
                subtask_data["user_id"] = user_id
            if time_estimated is not None:
                subtask_data["time_estimated"] = time_estimated
            if time_spent is not None:
                subtask_data["time_spent"] = time_spent
            if status is not None:
                subtask_data["status"] = status
            
            success = client.call_api("update_subtask", **subtask_data)
            return {
                "success": True,
                "data": {"updated": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error updating subtask {subtask_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def removeSubtask(subtask_id: int) -> Dict[str, Any]:
        """Remove (delete) a subtask.
        
        Args:
            subtask_id: The ID of the subtask to remove
        """
        try:
            success = client.call_api("remove_subtask", subtask_id)
            return {
                "success": True,
                "data": {"removed": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error removing subtask {subtask_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }