import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router
from app.logging_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("FastAPI application starting")
    yield
    logger.info("FastAPI application stopping")

app = FastAPI(title="Railway Backend Scaffold", version="0.1.0", lifespan=lifespan)
app.include_router(router)
