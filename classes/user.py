import classes.sql as sql

class User(object):
    def __init__(self):
        self.loggedIn = False
        self.__id = 0
        self.username = ""
        self.login_callback = lambda : print("")
        self.logout_callback = lambda : print("")

    def get_id(self):
        return self.__id

    def set_callback(self, login, logout):
        self.login_callback = login
        self.logout_callback = logout

    def login(self, username, password, sql_connection:sql.SqlConnector):
        response = sql_connection.login(username, password)
        if len(response) > 0:
            self.__id = response[0][0]
            self.username = response[0][1]
            self.loggedIn = True
            self.login_callback()

    def logout(self):
        self.__id = 0
        self.username = ""
        self.loggedIn = False
        self.login_callback()
