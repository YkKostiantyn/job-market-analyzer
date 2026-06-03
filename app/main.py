import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import init_db

from app.api.jobs import router as jobs_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Connecting to MongoDB...")
    try:
        await init_db()
        logger.info("Successfully connected to the database.")
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        raise e
    
    yield
    
    logger.info("Disconnecting from MongoDB")

app = FastAPI(title="Job Intelligence Platform", lifespan=lifespan)

app.include_router(jobs_router, prefix="")

@app.get("/health", tags=["System"])
async def health_check():
    logger.info("health-check")
    return {"status": "working", "db": "connected"}