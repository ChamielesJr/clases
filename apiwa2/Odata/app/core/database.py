
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar variables del archivo .env
load_dotenv()

# Leer la variable DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Validar que esté definida
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")

# Crear el motor de SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear la sesión de base de datos
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Declarar la base para los modelos
Base = declarative_base()

# Función para crear tablas automáticamente si no existen
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with SessionLocal() as session:
        yield session