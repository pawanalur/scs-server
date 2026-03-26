from datetime import datetime
from sqlalchemy import Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class EnergyDetail(Base):
    __tablename__ = "energy_details"

    energy_detail_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    energy_alert_id: Mapped[int] = mapped_column(ForeignKey("energy_alerts.energy_alert_id"))
    physical_energy: Mapped[float] = mapped_column(Float)
    mental_energy: Mapped[float] = mapped_column(Float)
    last_updated: Mapped[datetime] = mapped_column(DateTime)
    physical_drain_per_min: Mapped[float] = mapped_column(Float)
    mental_drain_per_min: Mapped[float] = mapped_column(Float)