from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class ExerciseDetail(Base):
    __tablename__ = "exercise_details"

    #
    exercise_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    action_id: Mapped[int] = mapped_column(ForeignKey("actions.action_id"))
    calorie_burnt: Mapped[float] = mapped_column(Float)
    type: Mapped[str] = mapped_column(String)
    physical_energy_change: Mapped[float] = mapped_column(Float)