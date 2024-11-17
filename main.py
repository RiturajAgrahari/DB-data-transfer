from pg import db_init
from models import BotUsage
import asyncio
from mydb import get_query


async def main():
    output = get_query()
    await db_init()
    new_usage = await BotUsage.all().values()
    print(new_usage)
    await BotUsage.all().delete()
    id = 0
    for row in output:
        id = row[0]
        print(f"Inserting id : {id} in postgres....", end=" --> ")
        try:
            usage = BotUsage(id=row[0], date=row[1], fandom_bot=row[2], lucky_bot=row[3], rpg_bot=row[4])
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
            usage = BotUsage(
                id=id,
                date=new_data["date"],
                fandom_bot=new_data["fandom_bot"],
                lucky_bot=new_data["lucky_bot"],
                rpg_bot=new_data["rpg_bot"]
            )
            await usage.save()
        except Exception as e:
            print(f"[ EXCEPTION ] at id : {id} :")
            print(e)
            print("-------------")
        print("Insertion complete!")


if __name__ == "__main__":
    asyncio.run(main())


"""
 id |    date    | fandom_bot | lucky_bot | rpg_bot 
----+------------+------------+-----------+---------
  6 | 2024-11-14 |          1 |        76 |       0
  8 | 2024-11-15 |          4 |        51 |       0
  1 | 2024-11-11 |          7 |        31 |       0


"""
