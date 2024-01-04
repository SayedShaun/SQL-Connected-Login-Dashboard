from dbhelper import Database
import sys


class LoginSystem:
    def __init__(self):
        self.db = Database()
        self.menu()

    def menu(self):
        user_input = input(
"""
Enter 1 for Registration:
Enter 2 for Login:
Enter 3 for Reset Password:
Enter 4 to Exit System
""" 
        )
        if user_input == "1":
            self.registration()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.reset_password()
        else:
            sys.exit(0)

    def content(self):
        user_input = input(
"""
Enter 1 to View Profile:
Enter 2 to Logout:
"""
        )
        if user_input == "1":
            print("Your Profile Looks Nice")
        elif user_input == "2":
            self.menu()

    def registration(self):
        name = input("Enter Name: ")
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")

        register = self.db.register(name, email, password)
        if register:
            print("Registration Successful")
            print("Please Login")
            self.login()
        else:
            print("Registration Unsuccessful")
            self.menu()

    def login(self):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")
        user_data = self.db.search(email, password)

        if not user_data:
            print("Incorrect email/password!!! Please try again")
            self.login()
        else:
            print("Hello", user_data[0][1])
            self.content()

    def reset_password(self):
        email = input("Enter Your Email: ")

        if not self.db.search_by_email(email):
            print("No Email Address Found!!! Please Login")
            self.login()
        else:
            new_password = input("Enter New Password: ")
            self.db.update_password(email, new_password)
            print("Password Reset Successful")


login_system = LoginSystem()
