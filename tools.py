## Importing libraries and files
import os
from dotenv import load_dotenv
from typing import Optional, Type
from pydantic import BaseModel
from langchain_community.document_loaders import PyPDFLoader
from crewai.tools import BaseTool
from crewai_tools import SerperDevTool

load_dotenv()

# Search tool instance
search_tool = SerperDevTool()

# Input schema
class BloodTestInput(BaseModel):
    query: Optional[str] = None

# Blood test reader tool
class BloodTestReportTool(BaseTool):
    name: str = "Read Blood Test Report"
    description: str = "Reads and returns contents of a blood test report PDF file"
    args_schema: Type[BaseModel] = BloodTestInput

    def _run(self, query: Optional[str] = None) -> str:
        try:
            # Use the default sample file for now
            file_path = "data/sample.pdf"
            docs = PyPDFLoader(file_path=file_path).load()
            full_report = "\n".join([d.page_content for d in docs])
            if not full_report.strip():
                return "No content found in PDF file"
            return full_report.strip()
        except Exception as e:
            return f"Could not read PDF file: {str(e)}"

    def _arun(self, query: Optional[str] = None):
        raise NotImplementedError("Async not supported for this tool.")

# Nutrition tool
class NutritionTool(BaseTool):
    name: str = "Nutrition Analysis"
    description: str = "Analyzes blood report data and suggests nutritional advice"
    args_schema: Type[BaseModel] = BloodTestInput

    def _run(self, query: Optional[str] = None) -> str:
        return "Nutrition analysis: Based on your blood work, I recommend adding more leafy greens and reducing processed foods. Consider vitamin D supplementation."

    def _arun(self, query: Optional[str] = None):
        raise NotImplementedError("Async not supported for this tool.")

# Exercise tool
class ExerciseTool(BaseTool):
    name: str = "Exercise Planning"
    description: str = "Creates an exercise plan based on blood report data"
    args_schema: Type[BaseModel] = BloodTestInput

    def _run(self, query: Optional[str] = None) -> str:
        return "Exercise plan: Start with 30 minutes of moderate cardio 3x per week. Add strength training 2x per week. Monitor heart rate and adjust intensity based on your blood pressure readings."

    def _arun(self, query: Optional[str] = None):
        raise NotImplementedError("Async not supported for this tool.")