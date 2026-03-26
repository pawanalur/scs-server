from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

USER = "sa"
PASSWORD = "Qwerty!23"
HOST = "127.0.0.1:1433"
DATABASE = "SCS_DB"
SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://{USER}:{PASSWORD}@{HOST}/{DATABASE}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass