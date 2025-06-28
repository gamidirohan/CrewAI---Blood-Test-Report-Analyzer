# Blood Test Report Analyser

## 🐛 Bugs Fixed and Solutions

### Tool and Agent Integration Issues
- [x] Fixed tool validation errors:
   - Issue: CrewAI tools were receiving metadata instead of actual string inputs
   - Solution: Implemented proper Pydantic schema and simplified tool implementations
   - Changed `BloodTestReportTool` to use clear input validation

- [x] Agent Configuration Issues:
   - Issue: Incorrect parameter name `tool` instead of `tools` in agent definitions
   - Solution: Updated all agent definitions to use plural `tools` parameter
   - Fixed tool instance passing (was incorrectly using methods)

- [x] PDF Reading Issues:
   - Issue: Incompatible PDF loader causing errors
   - Solution: Switched to `PyPDFLoader` from `langchain_community.document_loaders`
   - Added better error handling for PDF reading failures

- [x] FastAPI Integration Issues:
   - Issue: File upload not working due to missing dependency
   - Solution: Added `python-multipart` package for file upload support
   - Added CORS middleware to allow frontend access

- [x] Frontend Issues:
   - Issue: Health check failing due to incorrect endpoint
   - Solution: Fixed health check URL from '/' to '/health'
   - Added proper error handling and response formatting

## 🚀 Setup and Usage Instructions

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Unix
   myenv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI app:
   ```bash
   uvicorn main:app --reload
   ```
   The app will be available at http://localhost:8000/

## 📚 API Documentation

### Endpoints

1. `GET /health`
   - Health check endpoint
   - Returns: `{"message": "Blood Test Report Analyser API is running"}`

2. `POST /analyze`
   - Analyzes blood test reports
   - Request:
     - Form data:
       - `file`: PDF file (required)
       - `query`: string (optional, default: "Summarise my Blood Test Report")
   - Response (JSON):
     ```json
     {
       "status": "success",
       "query": "your query",
       "analysis": "AI-generated analysis text",
       "file_processed": "original-filename.pdf"
     }
     ```

### Response Format
- All responses are JSON
- The analysis is provided as text in the response, not as a PDF
- The original file is not modified or returned

### Error Handling
- HTTP 500: Server errors (with error details)
- HTTP 404: Resource not found
- HTTP 400: Invalid request format

[GitHub Repository Link](https://github.com/your-username/blood-test-analyser-debug)

---

## ✅ Fixed, Working Code
This repository now contains a working version of the Blood Test Report Analyser. All major bugs have been fixed and the API is ready for use and testing.

## ✅ Comprehensive README.md

### Bugs Found and How They Were Fixed
- **PDFLoader Import Error:**
  - **Bug:** The PDF reading tool was missing the import for `PDFLoader`.
  - **Fix:** Added `from langchain.document_loaders import PDFLoader` to `tools.py`.
- **Frontend for API Testing:**
  - **Bug:** No easy way to test endpoints.
  - **Fix:** Added a simple HTML frontend at `/` to test all endpoints.
- **Endpoint Clarity:**
  - **Bug:** Health check endpoint was `/`, which conflicted with the frontend.
  - **Fix:** Moved health check to `/health`.
- **General:**
  - Other minor bugs and missing instructions were addressed as per the checklist.

### Setup and Usage Instructions

#### 1. Clone the Repository
```sh
git clone https://github.com/your-username/blood-test-analyser-debug.git
cd blood-test-analyser-debug
```

#### 2. Create and Activate Virtual Environment
```sh
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On Linux/Mac:
source myenv/bin/activate
```

#### 3. Install Required Libraries
```sh
pip install -r requirements.txt
```
**Note:** Ensure you have `langchain` installed for PDFLoader support. If you see errors, run:
```sh
pip install langchain
```

#### 4. Run the FastAPI App
```sh
uvicorn main:app --reload
```
The app will be available at [http://localhost:8000/](http://localhost:8000/)

#### 5. Access the Frontend
Open your browser and go to [http://localhost:8000/](http://localhost:8000/) to use the built-in API tester.

### API Documentation

#### **Health Check**
- **Endpoint:** `GET /health`
- **Response:** `{ "message": "Blood Test Report Analyser API is running" }`

#### **Analyze Blood Report**
- **Endpoint:** `POST /analyze`
- **Form Data:**
  - `file`: PDF file (required)
  - `query`: (optional) analysis question
- **Response:**
  - `status`: success or error
  - `query`: the query used
  - `analysis`: the analysis result
  - `file_processed`: name of the uploaded file

#### **Frontend**
- **Endpoint:** `GET /`
- **Description:** Loads a simple HTML page to test all endpoints interactively.

---

## Notes
- Make sure to import `PDFLoader` in `tools.py`:
  ```python
  from langchain.document_loaders import PDFLoader
  ```
- If you add new features or fix more bugs, update this README accordingly.

# Project Setup and Execution Guide

## Getting Started

### Install Required Libraries
```sh
# Activate your virtual environment first
.\myenv\Scripts\Activate.ps1

# Install required dependencies
uv pip install -r requirements.txt
```

### Running the FastAPI App
```sh

# Then run the app
uvicorn main:app --reload
```

### Example API Usage
- **Health Check:**
  - `GET /`
- **Analyze Blood Report:**
  - `POST /analyze` with form-data:
    - `file`: PDF file
    - `query`: (optional) analysis question

# You're All Not Set!
🐛 **Debug Mode Activated!** The project has bugs waiting to be squashed - your mission is to fix them and bring it to life.

## Debugging Instructions

1. **Identify the Bug**: Carefully read the code and understand the expected behavior.
2. **Fix the Bug**: Implement the necessary changes to fix the bug.
3. **Test the Fix**: Run the project and verify that the bug is resolved.
4. **Repeat**: Continue this process until all bugs are fixed.
