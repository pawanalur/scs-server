from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users" # This will be the actual table name in SQL Server

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    physical_energy = Column(Float, default=100.0)
    mental_energy = Column(Float, default=100.0)
    in_progress_action_id = Column(Integer, nullable=True)