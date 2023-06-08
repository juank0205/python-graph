import mysql.connector
from datetime import datetime

class SqlConnector(object):
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
                host=host,
                user=user,
                passwd=password,
                database=database
                )
        self.cursor = self.db.cursor()

    def select_users(self):
        self.cursor.execute("SELECT * FROM users;")
        return self.cursor.fetchall()

    def login(self, username, password):
        try:
            self.cursor.execute(f'SELECT * FROM users WHERE username="{username}" AND password="{password}";')
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            self.db.rollback()
            print("Data not valid, ", error)

    def register(self, username, password):
        try:
            self.cursor.execute(f'INSERT INTO users (username, password) VALUES ("{username}", "{password}");')
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def insert_graph(self, id:int , string:str):
        try:
            self.cursor.execute(f'INSERT INTO graphs (string, user_id, created) VALUES ("{string}", "{id}", "{datetime.now().date().strftime("%Y-%m-%d")}")')
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def insert_differential_equation(self, id:int, string:str, initial_x:int, initial_y:int):
        try:
            self.cursor.execute(f'INSERT INTO differential_equations (string, user_id, initial_x, initial_y, created) VALUES ("{string}", "{id}", "{initial_x}", "{initial_y}", "{datetime.now().date().strftime("%Y-%m-%d")}")')
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def get_user_graphs(self, id:int):
        try:
            self.cursor.execute(f'SELECT * FROM graphs WHERE user_id={id}')
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            self.db.rollback()
            print("Failed to insert data: ", error)
            return []

    def get_user_differential_equations(self, id:int):
        try:
            self.cursor.execute(f'SELECT * FROM differential_equations WHERE user_id={id}')
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            self.db.rollback()
            print("Failed to insert data: ", error)
            return []

# sql = SqlConnector("localhost", "user", "123456789", "python-graph")
# list = sql.login("test", "123")
# print(list)
