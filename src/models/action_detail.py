from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class ActionDetail(Base):
    __tablename__ = "action_details"

    #
    action_detail_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    action_id: Mapped[int] = mapped_column(ForeignKey("actions.action_id"))
    title: Mapped[str] = mapped_column(String)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    additional_key1: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    additional_value1: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    additional_key2: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    additional_value2: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    additional_key3: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    additional_value3: Mapped[Optional[str]] = mapped_column(String, nullable=True)