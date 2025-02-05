# CRUD Operations
from sqlalchemy.orm import Session
from . import models, schemas


def create_message(db: Session, message: schemas.TelegramMessageCreate):
    db_message = models.TelegramMessage(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_message(db: Session, db_id: str):
    return (
        db.query(models.TelegramMessage)
        .filter(models.TelegramMessage.db_id == db_id)
        .first()
    )


def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TelegramMessage).offset(skip).limit(limit).all()


def update_message(
    db: Session, db_id: str, message_update: schemas.TelegramMessageBase
):
    db_message = (
        db.query(models.TelegramMessage)
        .filter(models.TelegramMessage.db_id == db_id)
        .first()
    )
    if db_message:
        for key, value in message_update.dict().items():
            setattr(db_message, key, value)
        db.commit()
        db.refresh(db_message)
    return db_message


def delete_message(db: Session, db_id: str):
    db_message = (
        db.query(models.TelegramMessage)
        .filter(models.TelegramMessage.db_id == db_id)
        .first()
    )
    if db_message:
        db.delete(db_message)
        db.commit()
    return db_message
