from fastapi import APIRouter, Depends
from app.database.database import get_db, engine, SessionLocal
from app.Schema.competition_schema import *
from app.Model.competition_model import Competition
from sqlalchemy.orm import Session
from typing import List
from fastapi.encoders import jsonable_encoder

competition = APIRouter()

#get competition details
@competition.get("/competition/",response_model=List[CreateCompetition])
def AllUser(db:Session = Depends(get_db)):
    db_usercompetition = db.query(Competition).all()
    #db.commit()
    return db_usercompetition

#create competition details
@competition.post("/competitionadd/",response_model= CreateCompetition)
def AddCompetition(request:updateCompetition, db:Session = Depends(get_db)):

    new_competition = Competition(name = request.name, description = request.description, user_id = request.user_id, status = request.status)
    db.add(new_competition)
    db.commit()

    return new_competition

#update competition details
@competition.put("/competitionupdate/{id}", response_model=CreateCompetition)
def UpdateCompetition(id:str, request: updateCompetition, db:Session = Depends(get_db)):
    updated_competition=db.query(Competition).filter(Competition.id == id).first()
    if request.name:
        updated_competition.name = request.name
    if request.status:
        updated_competition.status = request.status
    if request.description:
        updated_competition.description = request.description
    db.commit()
    return updated_competition


#delete competition details
@competition.delete("/competitiondelete/{id}")
def DeleteCompetition(id:str, db:Session = Depends(get_db)):
    db.query(Competition).filter(Competition.id == id).delete(synchronize_session=False)
    db.commit()

    return {"message": "Competition deleted successfully"}
