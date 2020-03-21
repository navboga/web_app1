import mysql.connector

class ConnectionError(Exception): # Это пользовательское исключение создано для выбрасывания в основной код стандартной ошибки вместо mysql.connector.errors.ProgrammingError
    pass

class CredentialsError(Exception):
    pass

class SQLError(Exception):
    pass

class UseDb():
    def __init__(self, config: dict)->None:
        self.config=config


    def __enter__(self):
        try: # Заставляем рейзить нужную нам ошибку если поймали mysql.connector.errors.ProgrammingError
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.ProgrammingError as err:
            raise ConnectionError('Wrong login or password',err)

    def __exit__(self, exc_type, exc_val, exc_tb)->None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()



# dbconfig = {
#     'host': '127.0.0.1',
#     'user': 'web_app',#vsearch
#     'password': 'web_app',#123
#     'database': 'vsearchlogDB',
#     }

# with UseDb(dbconfig) as cursor:
#     _SQL = """show tables"""
#     cursor.execute(_SQL)
#     data = cursor.fetchall()
# print(data)

