import os
import uvicorn

from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.organization import organization_router

if __name__ == '__main__':      
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
    exit()

metadata = [
    {
        "name": "Organization",
        "description": "Provides Organization CRUD"
    }
]

description = f"""
## DRAFTER API
# Drafter official API
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("-----API START-----")
    yield
    print("-----API END-----")

app = FastAPI(
    title="Drafter API",
    summary=f"Drafter API that provides functionally for the official Drafter website",
    description=description,
    version="0.0.1",
    contact={
        "name": "Francisco Fleury",
        "email": "franmeifleury@gmail.com",
    },
    openapi_tags=metadata,
    lifespan=lifespan
)

app.include_router(organization_router)