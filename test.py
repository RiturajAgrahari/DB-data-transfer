from mydb import get_query
from models import Profile
import asyncio
from pg import db_init


async def main():
    await db_init()
    print("Fetching MYSQL database data..")
    get_query()
    print("Fetching POSTGRESQL database data...")
    usage = await Profile.all().values()
    print("---DATA START ----")
    print(usage)
    print("---DATA END ----\n")


if __name__ == "__main__":
    asyncio.run(main())

