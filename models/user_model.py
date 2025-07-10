from pydantic import BaseModel, Field
from typing import Optional

class UserModel(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: Optional[str] = Field(default=None, alias="image")
