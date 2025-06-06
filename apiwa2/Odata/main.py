#cargamos las variables de entorno desde el archivo .env
from dotenv import load_dotenv
load_dotenv()

# Importación de la clase FastAPI para crear la aplicación
from fastapi import FastAPI
# Importación de los routers definidos en los módulos de rutas
from app.routes import R_Student, R_Classroom

# Inicialización de la aplicación FastAPI
app = FastAPI(title="API Estudiantes y Paralelos")

# Registro de rutas
app.include_router(R_Student.router)
app.include_router(R_Classroom.router)
