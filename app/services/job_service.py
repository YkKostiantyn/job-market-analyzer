import hashlib
from app.models.domain import JobPosting
from app.models.schemas import JobCreate
import logging

logger = logging.getLogger(__name__)

class JobService:
    async def create_job(self, job_data: JobCreate) -> JobPosting:
        
        raw_string = f"{job_data.title}-{job_data.company}-{job_data.source_url}"
        fingerprint = hashlib.md5(raw_string.encode()).hexdigest()

        existing_job = await JobPosting.find_one(JobPosting.fingerprint == fingerprint)
        if existing_job:
            logger.info(f"Job already exists: {job_data.title} at {job_data.company}")
            return existing_job

        new_job = JobPosting(
            **job_data.model_dump(),
            fingerprint=fingerprint
        )
        await new_job.insert()
        
        logger.info(f"Created new job: {new_job.title}")
        return new_job

job_service = JobService()