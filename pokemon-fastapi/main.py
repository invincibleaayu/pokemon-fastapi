from fastapi import FastAPI
from app.api.v1.routers import router
from app.core.config import settings

app = FastAPI()

app.include_router(router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Pokémon API"}
