from fastapi import APIRouter, Depends
from app.Schema.entry_schema import *
from app.Model.entry_model import Entry
from app.database.database import get_db, engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from fastapi.encoders import jsonable_encoder

entry = APIRouter()

#get entry details
@entry.get("/entry/",response_model=List[CreateEntry])
def AllEntry(db:Session = Depends(get_db)):
    db_entry = db.query(Entry).all()
    db.commit()
    return db_entry

#create entry details
@entry.post("/addentry/",response_model=CreateEntry)
def AddEntry(request: CreateEntry, db: Session = Depends(get_db)):
    new_entry = Entry(id = request.id, title = request.title, topic=request.topic, state=request.state, country= request.country, competition_id= request.competition_id)
    db.add(new_entry)
    db.commit()

    return new_entry

#update entry
@entry.put("/updateentry/{id}",response_model=CreateEntry)
def UpdateEntry(id:str, request : CreateEntry, db:Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).update(request.dict(exclude_unset=True))
    db.commit()
    updated_entry = db.query(Entry).filter(Entry.id == id).first()
    return updated_entry

#delete entry
@entry.delete("/deleteentry/{id}")
def DeleteEntry(id:str, db:Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).delete(synchronize_session=False)
    
    db.commit()

    return {"message": "Entry deleted successfully"}