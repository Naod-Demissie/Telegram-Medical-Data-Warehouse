# FastAPI Application & API Endpoints
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/messages/", response_model=schemas.TelegramMessageResponse)
def create_message(
    message: schemas.TelegramMessageCreate, db: Session = Depends(get_db)
):
    return crud.create_message(db, message)


@app.get("/messages/{db_id}", response_model=schemas.TelegramMessageResponse)
def read_message(db_id: str, db: Session = Depends(get_db)):
    message = crud.get_message(db, db_id)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return message


@app.get("/messages/", response_model=list[schemas.TelegramMessageResponse])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_messages(db, skip=skip, limit=limit)


@app.put("/messages/{db_id}", response_model=schemas.TelegramMessageResponse)
def update_message(
    db_id: str,
    message_update: schemas.TelegramMessageBase,
    db: Session = Depends(get_db),
):
    updated_message = crud.update_message(db, db_id, message_update)
    if updated_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return updated_message


@app.delete("/messages/{db_id}", response_model=schemas.TelegramMessageResponse)
def delete_message(db_id: str, db: Session = Depends(get_db)):
    deleted_message = crud.delete_message(db, db_id)
    if deleted_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return deleted_message


# Run with: uvicorn main:app --reload
