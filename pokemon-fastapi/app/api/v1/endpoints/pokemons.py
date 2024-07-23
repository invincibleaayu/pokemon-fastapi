from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.schemas.pokemon import Pokemon, PokemonCreate
from app.services.pokemon_service import PokemonService
from app.repositories.pokemon_repository import PokemonListingRepository
from app.core.db import get_db

router = APIRouter()

pokemon_listing_repository = PokemonListingRepository()
pokemon_service = PokemonService(pokemon_listing_repository)


@router.get("/", response_model=List[Pokemon])
async def read_pokemons(
    offset: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    name: Optional[str] = None,
    type_: Optional[str] = None,
):
    pokemons = await pokemon_service.get_pokemons(
        db, offset=offset, limit=limit, name=name, type_=type_
    )
    if not pokemons and name:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return pokemons


@router.post("/", response_model=Pokemon)
async def create_pokemon(pokemon: PokemonCreate, db: AsyncSession = Depends(get_db)):
    return await pokemon_service.create_pokemon(db, pokemon)
