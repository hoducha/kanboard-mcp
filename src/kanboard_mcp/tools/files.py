"""File-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register file-related tools."""
    
    @mcp.tool()
    def createTaskFile(task_id: int, filename: str, blob: str) -> Dict[str, Any]:
        """Create a new file attachment for a task.
        
        Args:
            task_id: The ID of the task to attach file to
            filename: The name of the file
            blob: The file content encoded in base64
        """
        try:
            file_id = client.call_api("create_task_file", task_id, filename, blob)
            return {
                "success": True,
                "data": {"file_id": file_id}
            }
        except KanboardClientError as e:
            logger.error(f"Error creating task file: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getAllTaskFiles(task_id: int) -> Dict[str, Any]:
        """Get all files attached to a task.
        
        Args:
            task_id: The ID of the task to get files for
        """
        try:
            files = client.call_api("get_all_task_files", task_id)
            return {
                "success": True,
                "data": files,
                "count": len(files) if files else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting all task files for task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getTaskFile(file_id: int) -> Dict[str, Any]:
        """Get a specific task file by ID.
        
        Args:
            file_id: The ID of the file to retrieve
        """
        try:
            file_info = client.call_api("get_task_file", file_id)
            return {
                "success": True,
                "data": file_info
            }
        except KanboardClientError as e:
            logger.error(f"Error getting task file {file_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def downloadTaskFile(file_id: int) -> Dict[str, Any]:
        """Download a task file.
        
        Args:
            file_id: The ID of the file to download
        """
        try:
            file_content = client.call_api("download_task_file", file_id)
            return {
                "success": True,
                "data": {"content": file_content}
            }
        except KanboardClientError as e:
            logger.error(f"Error downloading task file {file_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def removeTaskFile(file_id: int) -> Dict[str, Any]:
        """Remove (delete) a task file.
        
        Args:
            file_id: The ID of the file to remove
        """
        try:
            success = client.call_api("remove_task_file", file_id)
            return {
                "success": True,
                "data": {"removed": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error removing task file {file_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def removeAllTaskFiles(task_id: int) -> Dict[str, Any]:
        """Remove all files from a task.
        
        Args:
            task_id: The ID of the task to remove all files from
        """
        try:
            success = client.call_api("remove_all_task_files", task_id)
            return {
                "success": True,
                "data": {"removed": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error removing all task files for task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }