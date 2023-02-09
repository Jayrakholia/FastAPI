from pydantic import BaseModel
from typing import Optional
from app.utils.schemas import CommonSchemas


#demo for user
class Competitions(CommonSchemas):
    id: str
    name: str
    status: str
    description: str
    user_id: str

    class Config:
        orm_mode = True

#schema for take input and response
class CreateCompetition(BaseModel):
    id: Optional[str]
    name: str
    status: str
    description: str
    user_id: str

    class Config:
        orm_mode = True

#for update
class updateCompetition(BaseModel):
    id: Optional[str]
    name: Optional[str]
    status: Optional[str]
    description: Optional[str]
    user_id: Optional[str]

    class Config:
        orm_mode = True

