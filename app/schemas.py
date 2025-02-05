# Pydantic Schemas
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TelegramMessageBase(BaseModel):
    channel_name: str
    channel_address: str
    channel_id: int
    message_id: int
    date: datetime
    message: str
    cleaned_message: Optional[str] = None
    media_path: Optional[str] = None
    width: Optional[float] = None
    height: Optional[float] = None
    detections: str = "[]"


class TelegramMessageCreate(TelegramMessageBase):
    db_id: str


class TelegramMessageResponse(TelegramMessageBase):
    db_id: str

    class Config:
        from_attributes = True
