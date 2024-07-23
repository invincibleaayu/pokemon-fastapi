from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.pokemon_repository import PokemonListingRepository
from app.schemas.pokemon import PokemonCreate, Pokemon


class PokemonService:
    def __init__(self, listing_repository: PokemonListingRepository):
        self.listing_repository = listing_repository

    async def get_pokemons(
        self,
        db: AsyncSession,
        offset: int = 0,
        limit: int = 100,
        name: Optional[str] = None,
        type_: Optional[str] = None,
    ) -> List[Pokemon]:
        return await self.listing_repository.get_all(
            db, offset=offset, limit=limit, name=name, type_=type_
        )

    async def get_pokemon_by_name(
        self, db: AsyncSession, name: str
    ) -> Optional[Pokemon]:
        pokemons = await self.listing_repository.get_by_name(db, name=name)
        return pokemons[0] if pokemons else None

    async def get_pokemons_by_type(self, db: AsyncSession, type_: str) -> List[Pokemon]:
        return await self.listing_repository.get_by_type(db, type_=type_)

    async def create_pokemon(self, db: AsyncSession, pokemon: PokemonCreate) -> Pokemon:
        db_pokemon = Pokemon(**pokemon.__dict__)
        return await self.listing_repository.create(db, db_pokemon)
