from typing import List, Optional
from datetime import datetime
from beanie import Document
from pydantic import Field

class JobPosting(Document):
    title: str
    company: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    currency: Optional[str] = "USD"
    location: str
    skills: List[str] = Field(default_factory=list)
    source_url: str
    fingerprint: str = Field(unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "normalized_jobs"