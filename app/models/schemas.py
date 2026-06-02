from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from beanie import PydanticObjectId

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    source_url: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    currency: Optional[str] = "USD"
    skills: List[str] = Field(default_factory=list)

class JobResponse(JobCreate):
    id: PydanticObjectId
    fingerprint: str
    created_at: datetime

    class Config:
        json_encoders = {
            PydanticObjectId: str
        }