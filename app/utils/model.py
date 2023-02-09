from sqlalchemy import Column , DateTime , Boolean
from datetime import datetime


class Commonmodel:
    is_active = Column(Boolean,default=True )
    is_delete = Column(Boolean , default=False)
    created_at = Column(DateTime, default = datetime.utcnow)
    update_at = Column(DateTime , default = datetime.utcnow,onupdate=datetime.utcnow)

    def update_table(self, payload: dict):
        for key, value in payload.items():
            if value is not None:
                setattr(self, key, value)