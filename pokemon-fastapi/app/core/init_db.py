import asyncio
import httpx
from app.models.pokemon import Pokemon
from app.core.db import async_session, engine
from app.models.pokemon import Base
from app.core.config import settings


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        async with session.begin():
            async with httpx.AsyncClient(timeout=30.0) as client:  # Increased timeout
                try:
                    response = await client.get(settings.POKEAPI_URL)
                    response.raise_for_status()  # Raise an error for bad responses
                    data = response.json()
                    print(data, "\n\n\n")
                    for item in data["results"]:
                        try:
                            detail_response = await client.get(item["url"])
                            detail_response.raise_for_status()  # Raise an error for bad responses
                            detail_data = detail_response.json()

                            new_pokemon = Pokemon(
                                id=detail_data["id"],
                                name=detail_data["name"],
                                image=detail_data["sprites"]["front_default"],
                                type=detail_data["types"][0]["type"]["name"],
                            )
                            session.add(new_pokemon)
                        except httpx.HTTPStatusError as e:
                            print(f"Failed to fetch details for {item['name']}: {e}")
                except httpx.HTTPStatusError as e:
                    print(f"Failed to fetch initial Pokemon data: {e}")

        await session.commit()


if __name__ == "__main__":
    asyncio.run(init_db())
