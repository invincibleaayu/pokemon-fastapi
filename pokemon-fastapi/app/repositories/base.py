from typing import Any, List, Optional, Type, TypeVar, Generic
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import as_declarative, declared_attr
from sqlalchemy import func

T = TypeVar("T", bound="Base")


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> T:
        return await db.get(self.model, id)

    async def create(self, db: AsyncSession, obj_in: T) -> T:
        db.add(obj_in)
        await db.commit()
        await db.refresh(obj_in)
        return obj_in

    async def update(self, db: AsyncSession, db_obj: T, obj_in: Any) -> T:
        obj_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            setattr(db_obj, field, obj_data[field])
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, id: Any) -> T:
        obj = await db.get(self.model, id)
        await db.delete(obj)
        await db.commit()
        return obj

    async def list(
        self,
        db: AsyncSession,
        offset: int = 0,
        limit: int = 100,
        name: Optional[str] = None,
        type_: Optional[str] = None,
    ) -> List[T]:
        query = select(self.model).offset(offset).limit(limit)
        if name:
            query = query.where(self.model.name.ilike(f"%{name}%"))
        if type_:
            query = query.where(self.model.type.ilike(f"%{type_}%"))
        result = await db.execute(query)
        print(result, "\n\n\n\n")
        return result.scalars().all()

    async def count(self, db: AsyncSession) -> int:
        result = await db.execute(select(func.count()).select_from(self.model))
        return result.scalar()
