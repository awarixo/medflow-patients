from fastapi import FastAPI
from app import models
from app.database import engine
from app.api import router as api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Clinic Patient Records API",
    description="API for managing patient records in the clinic dashboard."
)

app.include_router(api_router)