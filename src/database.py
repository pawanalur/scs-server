from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

USER = "sa"
PASSWORD = "Qwerty!23"
HOST = "127.0.0.1:1433"
DATABASE = "SCS_DB"
SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()