from decouple import config
from database.db import Database
from database.users import Users

connection : Database= Database(
    host = config("HOST",str),
    port=config("PORT",int),
    user=config('USER',str),
    password=config('PASSWORD',str),
    db_name=config('DB_NAME',str)
)

def main():
    connection.create_table()
    # Users.insert_user(
    #     conn=connection.conn,
    #     login='glebix',
    #     password='123qwerty',
    #     age=21
    # )

    #метод поиска пользователя по любому одному параметру
    Users.find_user(conn=connection.conn,login = 'glebix')


if __name__=="__main__":
    main()



