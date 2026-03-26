from typing import Optional
from datetime import datetime
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Action(Base):
    __tablename__ = "actions"

    #
    action_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    action_type: Mapped[str] = mapped_column(String)
    start_at: Mapped[datetime] = mapped_column(DateTime)
    end_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    duration: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    is_discarded: Mapped[bool] = mapped_column(Boolean, default=False)
    is_in_progress: Mapped[bool] = mapped_column(Boolean, default=False)