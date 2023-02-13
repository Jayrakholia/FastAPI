from fastapi import APIRouter, Depends, HTTPException
from app.Schema.entry_schema import *
from app.Model.entry_model import Entry
from app.Model.competition_model import Competition
from app.Model.user_model import User
from app.database.database import get_db, engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from fastapi.encoders import jsonable_encoder

entry = APIRouter()

#get entry details
@entry.get("/entry/",response_model=List[CreateEntry])
def AllEntry(db:Session = Depends(get_db)):
    db_entry = db.query(Entry).all()
    print(type(db_entry))
    db.commit()

    return db_entry

@entry.get("/entry/{title}", response_model=  List[Response])
def entry_by_name(title, db:Session = Depends(get_db)):
    first= []
    second = []
    """ To generate information about particular entry.
    Args:
        name (_type_): Provide name of entry
    Returns:
        dict: return dict type value
    """
    dbEntry = db.query(Entry.competition_id).filter(Entry.title==title).all()
    for i in dbEntry:
        first.append(i[0])
    dbCompetition = db.query(Competition.user_id).filter(Competition.id.in_(first))
    
    for i in dbCompetition:
        second.append(i[0])
    set(second)
    dbUser = db.query(User).filter(User.id.in_(second)).all()
    
    if dbUser is None:
        
        return Error(error= "{} is not valid entry".format(title))
    
    return dbUser



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
    updated_entry=db.query(Entry).filter(Entry.id == id).first()
    if request.title:
        updated_entry.title = request.title
    if request.topic:
        updated_entry.topic = request.topic
    if request.state:
        updated_entry.state = request.state
    if request.country:
        updated_entry.country = request.country
    db.commit()
    return updated_entry
    

#delete entry
@entry.delete("/deleteentry/{id}")
def DeleteEntry(id:str, db:Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).delete(synchronize_session=False)
    
    db.commit()

    return {"message": "Entry deleted successfully"}