from tortoise import Tortoise
from dotenv import load_dotenv
import os

load_dotenv()


async def db_init():
    await Tortoise.init(
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "database": os.getenv("PG_DATABASE"),
                        "user": os.getenv("PG_USER"),
                        "host": os.getenv("PG_HOST"),
                        "port": os.getenv("PG_PORT"),
                        "password": os.getenv("PG_PASS"),
                    }
                }
            },
            "apps": {
                "models": {
                    "models": ["models"],
                    "default_connections": "default"
                }
            }
        }
    )
    await Tortoise.generate_schemas(safe=True)