import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("MY_SQL_HOST")
USER = os.getenv("MY_SQL_USER")
PASSWORD = os.getenv("MY_SQL_PASSWORD")
DATABASE = os.getenv("MY_SQL_DATABASE")


def open_database():
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        auth_plugin="mysql_native_password"
    )
    return mydb


def get_query():
    mydb = open_database()
    my_cursor = mydb.cursor()
    my_cursor.execute(f"SELECT * FROM bot_info;")
    output = my_cursor.fetchall()
    print("MYSQL - [ bot_info ] ALL DATA:")
    print(output)
    print(f"-----------------------------")
    mydb.close()
    return output


def main():
    get_query()


if __name__ == "__main__":
    main()