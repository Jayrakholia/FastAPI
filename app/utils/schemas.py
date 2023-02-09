from pydantic import BaseModel
from datetime import date
from typing import Optional

class CommonSchemas(BaseModel):
    created_at: Optional[date]
    updated_at: Optional[date]
    is_active: Optional[bool]
    is_delete: Optional[bool]