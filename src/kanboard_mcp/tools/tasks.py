"""Task-related tools for Kanboard MCP Server."""

from typing import Any, Dict, List, Optional, Union
import logging

from mcp.server.fastmcp import FastMCP

from ..client import KanboardClient, KanboardClientError


logger = logging.getLogger(__name__)


def register_tools(mcp: FastMCP, client: KanboardClient) -> None:
    """Register task-related tools."""
    
    @mcp.tool()
    def getAllTasks(project_id: int, status_id: Optional[int] = None) -> Dict[str, Any]:
        """Get all tasks for a project.
        
        Args:
            project_id: The ID of the project to get tasks for
            status_id: Optional status ID to filter tasks
        """
        try:
            if status_id is not None:
                tasks = client.call_api("get_all_tasks", project_id, status_id)
            else:
                tasks = client.call_api("get_all_tasks", project_id)
            
            return {
                "success": True,
                "data": tasks,
                "count": len(tasks) if tasks else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting all tasks for project {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getTask(task_id: int) -> Dict[str, Any]:
        """Get a specific task by ID.
        
        Args:
            task_id: The ID of the task to retrieve
        """
        try:
            task = client.call_api("get_task", task_id)
            return {
                "success": True,
                "data": task
            }
        except KanboardClientError as e:
            logger.error(f"Error getting task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getTaskByReference(project_id: int, reference: str) -> Dict[str, Any]:
        """Get a specific task by reference.
        
        Args:
            project_id: The ID of the project
            reference: The reference of the task to retrieve
        """
        try:
            task = client.call_api("get_task_by_reference", project_id, reference)
            return {
                "success": True,
                "data": task
            }
        except KanboardClientError as e:
            logger.error(f"Error getting task with reference '{reference}' in project {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getOverdueTasks() -> Dict[str, Any]:
        """Get all overdue tasks."""
        try:
            tasks = client.call_api("get_overdue_tasks")
            return {
                "success": True,
                "data": tasks,
                "count": len(tasks) if tasks else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting overdue tasks: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def getOverdueTasksByProject(project_id: int) -> Dict[str, Any]:
        """Get overdue tasks for a specific project.
        
        Args:
            project_id: The ID of the project to get overdue tasks for
        """
        try:
            tasks = client.call_api("get_overdue_tasks_by_project", project_id)
            return {
                "success": True,
                "data": tasks,
                "count": len(tasks) if tasks else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error getting overdue tasks for project {project_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def createTask(
        project_id: int,
        title: str,
        description: Optional[str] = None,
        category_id: Optional[int] = None,
        owner_id: Optional[int] = None,
        creator_id: Optional[int] = None,
        date_due: Optional[str] = None,
        color_id: Optional[str] = None,
        column_id: Optional[int] = None,
        swimlane_id: Optional[int] = None,
        priority: Optional[int] = None,
        reference: Optional[str] = None,
        tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Create a new task.
        
        Args:
            project_id: The ID of the project
            title: The title of the task
            description: The description of the task
            category_id: The category ID
            owner_id: The owner user ID
            creator_id: The creator user ID
            date_due: The due date (YYYY-MM-DD format)
            color_id: The color ID
            column_id: The column ID
            swimlane_id: The swimlane ID
            priority: The priority (0-3)
            reference: The reference
            tags: List of tags
        """
        try:
            task_data = {
                "project_id": project_id,
                "title": title,
            }
            
            # Add optional parameters
            if description is not None:
                task_data["description"] = description
            if category_id is not None:
                task_data["category_id"] = category_id
            if owner_id is not None:
                task_data["owner_id"] = owner_id
            if creator_id is not None:
                task_data["creator_id"] = creator_id
            if date_due is not None:
                task_data["date_due"] = date_due
            if color_id is not None:
                task_data["color_id"] = color_id
            if column_id is not None:
                task_data["column_id"] = column_id
            if swimlane_id is not None:
                task_data["swimlane_id"] = swimlane_id
            if priority is not None:
                task_data["priority"] = priority
            if reference is not None:
                task_data["reference"] = reference
            if tags is not None:
                task_data["tags"] = tags
            
            task_id = client.call_api("create_task", **task_data)
            return {
                "success": True,
                "data": {"task_id": task_id}
            }
        except KanboardClientError as e:
            logger.error(f"Error creating task: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def updateTask(
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        category_id: Optional[int] = None,
        owner_id: Optional[int] = None,
        date_due: Optional[str] = None,
        color_id: Optional[str] = None,
        priority: Optional[int] = None,
        reference: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update an existing task.
        
        Args:
            task_id: The ID of the task to update
            title: The new title of the task
            description: The new description of the task
            category_id: The new category ID
            owner_id: The new owner user ID
            date_due: The new due date (YYYY-MM-DD format)
            color_id: The new color ID
            priority: The new priority (0-3)
            reference: The new reference
        """
        try:
            task_data = {"id": task_id}
            
            # Add optional parameters
            if title is not None:
                task_data["title"] = title
            if description is not None:
                task_data["description"] = description
            if category_id is not None:
                task_data["category_id"] = category_id
            if owner_id is not None:
                task_data["owner_id"] = owner_id
            if date_due is not None:
                task_data["date_due"] = date_due
            if color_id is not None:
                task_data["color_id"] = color_id
            if priority is not None:
                task_data["priority"] = priority
            if reference is not None:
                task_data["reference"] = reference
            
            success = client.call_api("update_task", **task_data)
            return {
                "success": True,
                "data": {"updated": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error updating task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def openTask(task_id: int) -> Dict[str, Any]:
        """Open a task (set status to open).
        
        Args:
            task_id: The ID of the task to open
        """
        try:
            success = client.call_api("open_task", task_id)
            return {
                "success": True,
                "data": {"opened": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error opening task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def closeTask(task_id: int) -> Dict[str, Any]:
        """Close a task (set status to closed).
        
        Args:
            task_id: The ID of the task to close
        """
        try:
            success = client.call_api("close_task", task_id)
            return {
                "success": True,
                "data": {"closed": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error closing task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def removeTask(task_id: int) -> Dict[str, Any]:
        """Remove (delete) a task.
        
        Args:
            task_id: The ID of the task to remove
        """
        try:
            success = client.call_api("remove_task", task_id)
            return {
                "success": True,
                "data": {"removed": success}
            }
        except KanboardClientError as e:
            logger.error(f"Error removing task {task_id}: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    @mcp.tool()
    def searchTasks(
        project_id: int,
        query: str,
        category_id: Optional[int] = None,
        owner_id: Optional[int] = None,
        due_date: Optional[str] = None,
        status_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Search tasks in a project.
        
        Args:
            project_id: The ID of the project to search in
            query: The search query
            category_id: Optional category ID to filter
            owner_id: Optional owner user ID to filter
            due_date: Optional due date to filter (YYYY-MM-DD format)
            status_id: Optional status ID to filter
        """
        try:
            search_params = {
                "project_id": project_id,
                "query": query
            }
            
            # Add optional filters
            if category_id is not None:
                search_params["category_id"] = category_id
            if owner_id is not None:
                search_params["owner_id"] = owner_id
            if due_date is not None:
                search_params["due_date"] = due_date
            if status_id is not None:
                search_params["status_id"] = status_id
            
            tasks = client.call_api("search_tasks", **search_params)
            return {
                "success": True,
                "data": tasks,
                "count": len(tasks) if tasks else 0
            }
        except KanboardClientError as e:
            logger.error(f"Error searching tasks: {e}")
            return {
                "success": False,
                "error": str(e)
            }