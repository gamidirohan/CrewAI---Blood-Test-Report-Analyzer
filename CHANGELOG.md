# Changelog

This file documents all changes made to the project, including bug fixes, enhancements, and dependency updates. Add a new entry for each change you make.

## [Unreleased]
- Clarified API response format: returns JSON with text analysis, not PDF.
- Fixed tool validation errors by using proper Pydantic schema and simplified tool implementations.
- Changed agent parameter from `tool=` to `tools=` (plural) for correct CrewAI syntax.
- Simplified tool logic to avoid complex parameter handling that was causing validation issues.
- Improved error handling in BloodTestReportTool for better debugging.
- Fixed BloodTestReportTool validation error by correcting query parameter handling and file_path usage.
- Fixed frontend health check endpoint URL from '/' to '/health' to correctly test API status.
- Added CORS middleware to FastAPI app to allow frontend access to API endpoints.
- Switched from `PDFLoader` to `PyPDFLoader` from `langchain_community.document_loaders` for PDF reading.
- Refactored all tools (`BloodTestReportTool`, `NutritionTool`, `ExerciseTool`) to inherit from `crewai.tools.BaseTool` and use Pydantic schemas for CrewAI compatibility.
- Updated all agent definitions to use tool instances (not methods/functions) as required by CrewAI.
- Updated all task definitions to use tool instances (not methods/functions) as required by CrewAI.
- Fixed missing imports for `NutritionTool` and `ExerciseTool` in `agents.py`.
- Fixed FastAPI error by installing `python-multipart` for file upload support.
- Added documentation and code comments for tool and agent/task compatibility.
- Updated README and instructions to reflect new tool and agent/task patterns.
- Updated README to recommend running the app with `uvicorn main:app --reload` instead of `python main.py` for proper hot-reload support.
- Fixed SerperDevTool import and instantiation to match CrewAI documentation.
- General code cleanup and improved error handling for tool/agent/task integration.

---

Add new entries above this line as you make further changes.