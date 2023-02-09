from fastapi import APIRouter, Depends
from app.database.database import get_db
from app.Schema.user_schema import *
from app.Model.user_model import User
from sqlalchemy.orm import Session
from typing import List
from app.utils.model import Commonmodel

userdata = APIRouter()



#get user details
@userdata.get("/user/",tags=['users'],response_model=List[DisplayUsers])
def AllUser(db:Session = Depends(get_db)):
    db_users = db.query(User).all()
    return db_users

#create new user
@userdata.post("/user/",response_model=DisplayUsers)
def add_users(request:CreateUsers, db:Session=Depends(get_db)):
    new_users = User(name = request.name, birth_date = request.birth_date, gender = request.gender)
    db.add(new_users)
    db.commit()
    
    return new_users

#update user details


@userdata.put("/updateuser/{id}",response_model=DisplayUsers)
def UpdateUsers(id:str, request: updateUsers, db:Session = Depends(get_db)):
    updated_user= db.query(User).filter(User.id == id).first()
    if request.name:
        updated_user.name = request.name
    if request.birth_date:
        updated_user.birth_date = request.birth_date
    if request.gender:
        updated_user.gender = request.gender
    db.commit()
    return updated_user
    
    """updated_user = db.query(User).filter(User.id == id).first()
    payload = request.dict()
    updated_user.update_table(payload)
    db.commit()
    db.refresh(updated_user)

    return updated_user"""


#delete user details
@userdata.delete("/deleteuser/{id}")
def DeleteUser(id:str, db:Session = Depends(get_db)):
    db.query(User).filter(User.id == id).delete(synchronize_session=False)
    db.commit()

    return {"message": "User deleted successfully"}




