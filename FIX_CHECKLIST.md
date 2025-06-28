# Debug Assignment: Component-wise Fix Checklist

Use this checklist to track and prioritize bug fixes and improvements for each component of the repo. Check off items as you complete them.

## 1. Setup & Documentation
- [x] Fix typo in README: `requirement.txt` → `requirements.txt`
- [x] Add missing instructions for running the FastAPI app
- [x] Add usage examples for API endpoints
- [x] Add requirements for all dependencies in `requirements.txt`

## 2. main.py (API & App Logic)
- [ ] Ensure all required agents and tasks are imported and used correctly
- [ ] Add support for all defined agents and tasks (not just `doctor` and `help_patients`)
- [ ] Improve error handling and logging
- [ ] Add input validation for uploaded files

## 3. agents.py (Agents)
- [ ] Fix undefined `llm` (define or import a valid LLM instance)
- [ ] Ensure all agents use correct tools and LLMs
- [ ] Remove or update unrealistic/unsafe agent behaviors
- [ ] Add tests for agent logic

## 4. task.py (Tasks)
- [ ] Ensure each task uses the correct agent (not just `doctor`)
- [ ] Add missing tasks to the main workflow
- [ ] Improve task descriptions and expected outputs for clarity

## 5. tools.py (Tools)
- [ ] Import or implement `PDFLoader` for PDF reading
- [ ] Complete implementation of `NutritionTool` and `ExerciseTool`
- [ ] Add error handling for file operations
- [ ] Add tests for tool functionality

## 6. General
- [ ] Add automated tests for API endpoints
- [ ] Add linting/formatting configuration
- [ ] Clean up unused code and comments

---

Check off each item as you address it. Update this file as new issues are discovered or resolved.
