from fastapi import FastAPI, File, UploadFile, Form, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
import asyncio
import psycopg2
from dotenv import load_dotenv
from celery import Celery

from crewai import Crew, Process
from agents import doctor
from task import help_patients

app = FastAPI(title="Blood Test Report Analyser")

# Import Celery app
from celery import current_app as celery_app

# Initialize database
from db_init import create_table
create_table()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

def get_db_connection():
    """Establish database connection"""
    load_dotenv()
    try:
        connection = psycopg2.connect(
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
            dbname=os.getenv("dbname")
        )
        return connection
    except Exception as e:
        print(f"Database connection error: {e}")
        raise

def run_crew(query: str, file_path: str="data/sample.pdf"):
    """To run the whole crew"""
    # Update the BloodTestReportTool to use the actual uploaded file
    from tools import BloodTestReportTool
    
    # Create a modified version of the task that includes the file path
    medical_crew = Crew(
        agents=[doctor],
        tasks=[help_patients],
        process=Process.sequential,
    )
    
    # Pass both query and file_path context
    result = medical_crew.kickoff({
        'query': query,
        'file_path': file_path
    })
    return result

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse("static/index.html")

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report"),
    background_tasks: BackgroundTasks = None
):
    """Analyze blood test report and provide comprehensive health recommendations"""
    
    # Generate unique filename to avoid conflicts
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    
    try:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Validate query
        if query=="" or query is None:
            query = "Summarise my Blood Test Report"
            
        # Queue the analysis task
        task = app.celery.send_task('analyze_task', args=[query, file_path, file.filename])
        
        return JSONResponse({
            "status": "queued",
            "task_id": task.id,
            "message": "Analysis request queued successfully"
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing blood report: {str(e)}")
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass  # Ignore cleanup errors

# Celery task
@app.celery.task(name='analyze_task')
def analyze_task(query, file_path, filename):
    """Celery task to process blood report"""
    try:
        response = run_crew(query=query.strip(), file_path=file_path)
        
        # Store results in database
        conn = None
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO blood_test_results 
                (query, analysis, file_name) 
                VALUES (%s, %s, %s)
                """, 
                (query, str(response), filename))
            conn.commit()
        except Exception as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
