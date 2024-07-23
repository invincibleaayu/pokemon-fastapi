from pydantic import BaseModel
from typing import List


class PokemonBase(BaseModel):
    name: str
    image: str
    type: List[str]


class PokemonCreate(PokemonBase):
    pass


class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True
