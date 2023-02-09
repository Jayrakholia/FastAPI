from app.database.database import Base
from sqlalchemy import Column, String, Date
from app.utils.model import Commonmodel
import uuid

def generate_uuid():
    return str(uuid.uuid4())


class User (Base, Commonmodel):
    __tablename__ = "user_table"
    id = Column(String,primary_key=True, default=generate_uuid)
    name = Column(String)
    birth_date = Column(Date)
    gender = Column(String)
