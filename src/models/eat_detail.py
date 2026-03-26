from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class EatDetail(Base):
    __tablename__ = "eat_details"

    #
    eat_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    action_id: Mapped[int] = mapped_column(ForeignKey("actions.action_id"))
    calorie_consumed: Mapped[float] = mapped_column(Float)
    sugar_consumed: Mapped[float] = mapped_column(Float)
    protein_consumed: Mapped[float] = mapped_column(Float)
    physical_energy_change: Mapped[float] = mapped_column(Float)