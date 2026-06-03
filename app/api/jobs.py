from fastapi import APIRouter
from app.models.schemas import JobCreate, JobResponse
from app.services.job_service import job_service

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobResponse, status_code=201)
async def create_new_job(job_in: JobCreate):
    job = await job_service.create_job(job_in)
    return job