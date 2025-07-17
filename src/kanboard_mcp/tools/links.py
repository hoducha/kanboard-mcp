"""Link-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register link-related tools."""
    
    @mcp.tool()
    def createTaskLink(task_id: int, opposite_task_id: int, link_id: int) -> Dict[str, Any]:
        """Create a link between two tasks.
        
        Args:
            task_id: The ID of the first task
            opposite_task_id: The ID of the second task to link to
            link_id: The ID of the link type
        """
        try:
            success = client.call_api("create_task_link", task_id, opposite_task_id, link_id)
            return {
                "success": True,
                "data": {"created": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error creating task link: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def updateTaskLink(task_link_id: int, task_id: int, opposite_task_id: int, link_id: int) -> Dict[str, Any]:
        """Update an existing task link.
        
        Args:
            task_link_id: The ID of the task link to update
            task_id: The ID of the first task
            opposite_task_id: The ID of the second task to link to
            link_id: The ID of the link type
        """
        try:
            success = client.call_api("update_task_link", task_link_id, task_id, opposite_task_id, link_id)
            return {
                "success": True,
                "data": {"updated": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error updating task link {task_link_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getTaskLinkById(task_link_id: int) -> Dict[str, Any]:
        """Get a specific task link by ID.
        
        Args:
            task_link_id: The ID of the task link to retrieve
        """
        try:
            link = client.call_api("get_task_link_by_id", task_link_id)
            return {
                "success": True,
                "data": link
            }
        except KanboardClientError as e:
            logger.error(f"Error getting task link {task_link_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getAllTaskLinks(task_id: int) -> Dict[str, Any]:
        """Get all links for a task.
        
        Args:
            task_id: The ID of the task to get links for
        """
        try:
            links = client.call_api("get_all_task_links", task_id)
            return {
                "success": True,
                "data": links,
                "count": len(links) if links else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting all task links for task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def removeTaskLink(task_link_id: int) -> Dict[str, Any]:
        """Remove (delete) a task link.
        
        Args:
            task_link_id: The ID of the task link to remove
        """
        try:
            success = client.call_api("remove_task_link", task_link_id)
            return {
                "success": True,
                "data": {"removed": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error removing task link {task_link_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getAllLinks() -> Dict[str, Any]:
        """Get all available link types."""
        try:
            links = client.call_api("get_all_links")
            return {
                "success": True,
                "data": links,
                "count": len(links) if links else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting all links: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getOppositeLinkId(link_id: int) -> Dict[str, Any]:
        """Get the opposite link ID for a given link.
        
        Args:
            link_id: The ID of the link to get the opposite for
        """
        try:
            opposite_id = client.call_api("get_opposite_link_id", link_id)
            return {
                "success": True,
                "data": {"opposite_link_id": opposite_id}
            }
        except KanboardClientError as e:
            logger.error(f"Error getting opposite link ID for {link_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getLinkByLabel(label: str) -> Dict[str, Any]:
        """Get a link by its label.
        
        Args:
            label: The label of the link to retrieve
        """
        try:
            link = client.call_api("get_link_by_label", label)
            return {
                "success": True,
                "data": link
            }
        except KanboardClientError as e:
            logger.error(f"Error getting link by label '{label}': {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getLinkById(link_id: int) -> Dict[str, Any]:
        """Get a link by its ID.
        
        Args:
            link_id: The ID of the link to retrieve
        """
        try:
            link = client.call_api("get_link_by_id", link_id)
            return {
                "success": True,
                "data": link
            }
        except KanboardClientError as e:
            logger.error(f"Error getting link {link_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def createLink(label: str, opposite_label: str) -> Dict[str, Any]:
        """Create a new link type.
        
        Args:
            label: The label of the link
            opposite_label: The label of the opposite link
        """
        try:
            link_id = client.call_api("create_link", label, opposite_label)
            return {
                "success": True,
                "data": {"link_id": link_id}
            }
        except KanboardClientError as e:
            logger.error(f"Error creating link: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def updateLink(link_id: int, label: str, opposite_label: str) -> Dict[str, Any]:
        """Update an existing link type.
        
        Args:
            link_id: The ID of the link to update
            label: The new label of the link
            opposite_label: The new label of the opposite link
        """
        try:
            success = client.call_api("update_link", link_id, label, opposite_label)
            return {
                "success": True,
                "data": {"updated": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error updating link {link_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def removeLink(link_id: int) -> Dict[str, Any]:
        """Remove (delete) a link type.
        
        Args:
            link_id: The ID of the link to remove
        """
        try:
            success = client.call_api("remove_link", link_id)
            return {
                "success": True,
                "data": {"removed": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error removing link {link_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }