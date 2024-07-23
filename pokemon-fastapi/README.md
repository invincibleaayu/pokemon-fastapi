# Pokemon FastAPI Project

This project is a FastAPI application to list and filter Pokémon using data from the PokeAPI. The data is stored in a PostgreSQL database and can be filtered by name and type.

## Project Structure

```plaintext
pokemon-api/
├── alembic/
│ ├── versions/
│ └── env.py
│ └── script.py.mako
├── app/
│ ├── api/
│ │ └── v1/
│ │ ├── init.py
│ │ ├── endpoints/
│ │ │ └── pokemons.py
│ │ └── router.py
│ ├── core/
│ │ ├── init.py
│ │ ├── config.py
│ │ ├── db.py
│ │ └── init_db.py
│ ├── models/
│ │ ├── init.py
│ │ ├── pokemon.py
│ ├── repositories/
│ │ ├── init.py
│ │ ├── base.py
│ │ ├── pokemon_repository.py
│ ├── schemas/
│ │ ├── init.py
│ │ ├── pokemon.py
│ ├── services/
│ │ ├── init.py
│ │ ├── pokemon_service.py
│ └── main.py
├── alembic.ini
├── .pre-commit-config.yaml
├── requirements.txt
├── README.md
└── .env
```
## Requirements

- Python 3.8+
- PostgreSQL
- Rye (for managing dependencies and running commands)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd pokemon-api
```
### 2. Install dependencies (for mac
  - Ensure you have Rye installed. If not, install it using:
```plaintext
curl -sSf https://rye.astral.sh/get | bash
```

### 3. Confugire Environment Variables
```bash
# core
API_V1_STR= /api/v1
DATABASE_URL= ""
POKEAPI_URL=https://pokeapi.co/api/v2/pokemon?limit=25

```
### 4. Initialize the Database
-To populate the database with Pokémon data, run:
```bash
rye run python -m app.core.init_db
```
###5.Run the project
```bash
cd pokemon-api
rye sync
rye run uvicorn app.main:app --reload
```
## Database Migration With ALembic
- If Alembic is not already initialized, run:
```bash
alembic init alembic
```
### Create New Migration
```bash
alembic revision --autogenerate -m "<Your message>"

```


