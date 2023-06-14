from database.db import Database

class Users:
    
    id:int
    login:str
    password:str
    age :int

    @staticmethod
    def insert_user(
        conn:Database,
        login:str,
        password:str,
        age:int
    ):
        try:
            with conn.cursor() as cur:
                cur.execute(F"""
                    INSERT INTO users(
                        login,
                        password,
                        age
                    ) VALUES(
                        '{login}',
                        '{password}',
                        {age}
                    );
                """)
                print("Пользователь с ником ",login,"Успешно добавлен")
        except Exception as e:
            print("Ошибка добавления: ",e)
    
    @staticmethod
    def find_user(conn:Database,**kwargs):
        for i , j in kwargs.items():
            if isinstance(j,str):
                for key ,value in kwargs.items():
                    try:
                        with conn.cursor() as cur:
                            cur.execute(f"""
                                SELECT * FROM users 
                                WHERE {key} = '{value}'
                            """)
                            result = cur.fetchall()
                            print(result)
                    except Exception as e:
                        print(e)
            else:
                for key ,value in kwargs.items():
                    try:
                        with conn.cursor() as cur:
                            cur.execute(f"""
                                SELECT * FROM users 
                                WHERE {key} = {value}
                            """)
                            result = cur.fetchall()
                            print(result)
                    except Exception as e:
                        print(e)
                
