from pydantic import BaseModel
from datetime import date
from typing import Optional


#demo for user
class Entry(BaseModel):
    id: str 
    title: str
    topic: str
    state: str
    country: str
    is_delete: bool
    created_at: date
    updated_at: date
    competition_id: str
    
    class Config:
        orm_mode = True

#schema for input and response

class CreateEntry(BaseModel):
    id: Optional[str] 
    title: str
    topic: str
    state: str
    country: str
    competition_id: str

    class Config:
        orm_mode = True

#for update
class CreateEntry(BaseModel):
    id: Optional[str] 
    title: Optional[str]
    topic: Optional[str]
    state: Optional[str]
    country: Optional[str]
    competition_id: Optional[str]

    class Config:
        orm_mode = True