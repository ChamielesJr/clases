# main.py
from dotenv import load_dotenv
load_dotenv()  

from fastapi import FastAPI
from app.routes import R_Student, R_Classroom

app = FastAPI(title="API Estudiantes y Paralelos")

app.include_router(R_Student.router)
app.include_router(R_Classroom.router)
