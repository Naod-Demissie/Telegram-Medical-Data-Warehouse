# SQLAlchemy Data Models
from .database import Base


class TelegramMessage(Base):
    __tablename__ = "telegram_messages"

    db_id = Column(String, primary_key=True, index=True)
    channel_name = Column(Text, nullable=False)
    channel_address = Column(Text, nullable=False)
    channel_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    message = Column(Text, nullable=False)
    cleaned_message = Column(Text, nullable=True)
    media_path = Column(Text, nullable=True)
    width = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    detections = Column(Text, nullable=False, default="[]")
