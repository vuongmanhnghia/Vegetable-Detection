from pydantic import BaseModel, Field
from typing import Optional


class History(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    image_url: str = Field(..., description="Image URL")
