# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2025-01-17

### Added
- Initial release of Kanboard MCP Server
- Complete implementation of 62+ Kanboard API tools organized by category:
  - Projects (5 tools): getAllProjects, getProjectById, getProjectByName, getProjectActivity, getProjectActivities
  - Tasks (11 tools): getAllTasks, getTask, getTaskByReference, getOverdueTasks, getOverdueTasksByProject, createTask, updateTask, openTask, closeTask, removeTask, searchTasks
  - Categories (2 tools): getCategory, getAllCategories
  - Columns (2 tools): getColumns, getColumn
  - Boards (1 tool): getBoard
  - Comments (5 tools): createComment, getComment, getAllComments, updateComment, removeComment
  - Users (9 tools): getUser, getUserByName, getAllUsers, getMe, getMyDashboard, getMyActivityStream, getMyProjectsList, getMyOverdueTasks, getMyProjects
  - Links (12 tools): createTaskLink, updateTaskLink, getTaskLinkById, getAllTaskLinks, removeTaskLink, getAllLinks, getOppositeLinkId, getLinkByLabel, getLinkById, createLink, updateLink, removeLink
  - Subtasks (5 tools): createSubtask, getSubtask, getAllSubtasks, updateSubtask, removeSubtask
  - Tags (4 tools): getAllTags, getTagsByProject, setTaskTags, getTaskTags
  - Files (6 tools): createTaskFile, getAllTaskFiles, getTaskFile, downloadTaskFile, removeTaskFile, removeAllTaskFiles
- Configuration management with environment variables
- Robust error handling and retry logic
- Comprehensive documentation and examples
- Claude Desktop integration examples
- Entry point script for easy execution

### Features
- Authentication using Kanboard API tokens
- Support for both application and user API authentication
- Configurable SSL verification and connection settings
- Debug mode for detailed logging
- Automatic retry on connection failures
- Type hints and validation throughout codebase

### Documentation
- Complete README with setup instructions
- API reference for all 62+ tools
- Claude Desktop configuration examples
- Troubleshooting guide
- Environment variable configuration guide

[Unreleased]: https://github.com/yourusername/kanboard-mcp/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/yourusername/kanboard-mcp/releases/tag/v0.1.0