from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class EnergyAlert(Base):
    __tablename__ = "energy_alerts"

    energy_alert_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    warning_high_physical: Mapped[float] = mapped_column(Float)
    warning_high_mental: Mapped[float] = mapped_column(Float)
    error_high_physical: Mapped[float] = mapped_column(Float)
    error_high_mental: Mapped[float] = mapped_column(Float)
    warning_low_physical: Mapped[float] = mapped_column(Float)
    warning_low_mental: Mapped[float] = mapped_column(Float)
    error_low_physical: Mapped[float] = mapped_column(Float)
    error_low_mental: Mapped[float] = mapped_column(Float)