"""Project-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register project-related tools."""
    
    @mcp.tool()
    def getAllProjects() -> Dict[str, Any]:
        """Get all projects from Kanboard."""
        try:
            projects = client.call_api("get_all_projects")
            return {
                "success": True,
                "data": projects,
                "count": len(projects) if projects else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting all projects: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getProjectById(project_id: int) -> Dict[str, Any]:
        """Get a specific project by ID.
        
        Args:
            project_id: The ID of the project to retrieve
        """
        try:
            project = client.call_api("get_project_by_id", project_id)
            return {
                "success": True,
                "data": project
            }
        except KanboardClientError as e:
            logger.error(f"Error getting project {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getProjectByName(project_name: str) -> Dict[str, Any]:
        """Get a specific project by name.
        
        Args:
            project_name: The name of the project to retrieve
        """
        try:
            project = client.call_api("get_project_by_name", project_name)
            return {
                "success": True,
                "data": project
            }
        except KanboardClientError as e:
            logger.error(f"Error getting project '{project_name}': {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getProjectActivity(project_id: int) -> Dict[str, Any]:
        """Get activity for a specific project.
        
        Args:
            project_id: The ID of the project to get activity for
        """
        try:
            activity = client.call_api("get_project_activity", project_id)
            return {
                "success": True,
                "data": activity,
                "count": len(activity) if activity else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting project activity for {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getProjectActivities(project_id: int) -> Dict[str, Any]:
        """Get activities for a specific project.
        
        Args:
            project_id: The ID of the project to get activities for
        """
        try:
            activities = client.call_api("get_project_activities", project_id)
            return {
                "success": True,
                "data": activities,
                "count": len(activities) if activities else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting project activities for {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }