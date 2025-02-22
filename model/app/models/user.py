from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional
from bcrypt import hashpw, gensalt


# Schema cho Book
class User(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")  # Alias cho MongoDB ObjectId
    email: str = Field(..., description="Email of the user")
    name: str = Field(..., description="Name of the user")
    picture: str = Field(..., description="Picture of the user")
    google_id: str = Field(..., description="Google ID of the user")

    class Config:
        populate_by_name = True


# Schema cho tạo user mới
class UserRegister(User):
    pass
