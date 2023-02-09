from app.database.database import Base
from sqlalchemy import Column, String, ForeignKey
from app.Model.user_model import User
from app.utils.model import Commonmodel
import uuid

def generate_uuid():
    return str(uuid.uuid4())


class Competition(Base,Commonmodel):
    __tablename__ = "competition_table"
    id = Column(String, primary_key = True,default=generate_uuid)
    name = Column(String)
    status = Column(String)
    description = Column(String)
    user_id=Column(String,ForeignKey(User.id))