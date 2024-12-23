from pg import db_init
from models import Profile
import asyncio
from mydb import get_query


async def main():
    output = get_query()
    await db_init()
    new_usage = await Profile.all().values()
    print(new_usage)
    await Profile.all().delete()
    id = 0
    for row in output:
        id = row[0]
        print(f"Inserting id : {id} in postgres....", end=" --> ")
        try:
            usage = Profile(id=row[0], discord_name=row[1], discord_id=row[2], bot_used=row[3])
            await usage.save()
        except Exception as e:
            print(f"[ EXCEPTION ] at id : {id} :")
            print(e)
            print("-------------")
        print("Insertion complete!")

    print("NEW DATA STARTED INSERTING:...")
    for new_data in new_usage:
        id += 1
        print(f"Inserting id : {id} in postgres....", end=" --> ")
        try:
            usage = Profile(
                id=id,
                discord_name=new_data["discord_name"],
                discord_id=new_data["discord_id"],
                bot_used=new_data["bot_used"],
            )
            await usage.save()
        except Exception as e:
            print(f"[ EXCEPTION ] at id : {id} :")
            print(e)
            print("-------------")
        print("Insertion complete!")


if __name__ == "__main__":
    asyncio.run(main())

# Botusage DONE

"""
 id |    date    | fandom_bot | lucky_bot | rpg_bot 
----+------------+------------+-----------+---------
  6 | 2024-11-14 |          1 |        76 |       0
  8 | 2024-11-15 |          4 |        51 |       0
  1 | 2024-11-11 |          7 |        31 |       0


"""
