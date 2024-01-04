import mysql.connector
import sys


class Database:
    def __init__(self):
        try:
            self.connection = (
                mysql.connector.connect(
                    host="localhost",
                    user="root", 
                    password="", 
                    database="sql-db")
                    )
            self.cursor = self.connection.cursor()
        except:
            print("Could not connect to Database")
            sys.exit(0)
        else:
            print("Connected to Database")

    def register(self, name, email, password):
        try:
            self.cursor.execute(
                f"INSERT INTO user (id, name, email, password) VALUES (NULL, '{name}', '{email}', '{password}')")
            self.connection.commit()
        except:
            return -1
        else:
            return 1

    def search(self, email, password):
        query = f"SELECT * FROM user WHERE email='{email}' AND password='{password}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def search_by_email(self, email):
        query = f"SELECT * FROM user WHERE email='{email}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_password(self, email, new_password):
        try:
            query = f"UPDATE user SET password='{new_password}' WHERE email='{email}'"
            self.cursor.execute(query)
            self.connection.commit()
        except:
            return -1
        else:
            return 1
