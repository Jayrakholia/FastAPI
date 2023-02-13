from app.database.database import Base
from sqlalchemy import Column, Boolean, String, ForeignKey, DateTime
from datetime import datetime
from app.Model.competition_model import Competition
import uuid
from sqlalchemy.orm import relationship

def generate_uuid():
    return str(uuid.uuid4())


class Entry(Base):
    __tablename__ = "entry_table"
    id = Column(String,primary_key=True,default=generate_uuid)
    title = Column(String)
    topic= Column(String)
    state = Column(String)
    country =Column(String)
    is_delete = Column(Boolean,default=False)
    created_at = Column(DateTime,default=datetime.utcnow)
    updated_at =Column(DateTime,default=datetime.utcnow)
    competition_id = Column(String, ForeignKey(Competition.id))
