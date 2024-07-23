from fastapi import APIRouter
from .endpoints import pokemons

router = APIRouter()

router.include_router(pokemons.router, prefix="/pokemons", tags=["Pokemons"])
