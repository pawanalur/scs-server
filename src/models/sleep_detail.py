from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class SleepDetail(Base):
    __tablename__ = "sleep_details"

    #
    sleep_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    action_id: Mapped[int] = mapped_column(ForeignKey("actions.action_id"))
    mental_energy_change: Mapped[float] = mapped_column(Float)