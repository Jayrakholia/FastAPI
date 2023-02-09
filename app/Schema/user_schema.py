from typing import Optional
from pydantic import BaseModel,Field
from datetime import date
from app.utils.schemas import CommonSchemas


#understand for user
class Users(CommonSchemas):
    id: str
    name: str
    birth_date: date
    gender: str

    class Config:
        orm_mode = True


#take input from user
class CreateUsers(BaseModel):
    name: str
    birth_date: Optional[date] = Field(default_factory=date(2002, 3, 9))
    gender:str

    class Config:
        orm_mode = True

#update input for user
class updateUsers(BaseModel):
    name: Optional[str]=None
    birth_date: Optional[date]=None #Field(default_factory=date(2002, 3, 9))
    gender: Optional[str]=None

    class Config:
        orm_mode = True

#for response
class DisplayUsers(BaseModel):
    id: Optional[str]
    name: Optional[str]
    birth_date: Optional[date]
    gender: Optional[str]
    
    #call schema for object (middle)
    class Config:
        orm_mode = True

    


