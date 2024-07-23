from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.pokemon import Pokemon
from app.repositories.base import BaseRepository


class PokemonListingRepository(BaseRepository[Pokemon]):
    def __init__(self):
        super().__init__(Pokemon)

    async def get_all(
        self,
        db: AsyncSession,
        offset: int = 0,
        limit: int = 100,
        name: Optional[str] = None,
        type_: Optional[str] = None,
    ) -> List[Pokemon]:
        return await self.list(db, offset=offset, limit=limit, name=name, type_=type_)

    async def get_by_name(self, db: AsyncSession, name: str) -> Optional[Pokemon]:
        return await self.get_all(
            db, offset=0, limit=100, name=name, type_=None
        )  # Filtering by name

    async def get_by_type(self, db: AsyncSession, type_: str) -> List[Pokemon]:
        return await self.get_all(
            db, offset=0, limit=100, name=None, type_=type_
        )  # Filtering by type
