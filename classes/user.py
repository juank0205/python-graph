import sql as sql

class User(object):
    def __init__(self):
        self.loggedIn = False
        self.__id = 0
        self.username = ""

    def get_id(self):
        return self.__id

    def login(self, username, password, sql_connection:sql.SqlConnector):
        response = sql_connection.login(username, password)
        if len(response) > 0:
            self.__id = response[0][0]
            self.username = response[0][1]
