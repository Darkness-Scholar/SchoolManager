# There are 2 types of users in the system
# Then, he/she can view his/her profile info, change password, or log out of the system

import random
from os import system
from llist import *

class User:
    def __init__(self, account, password, info):
        self.account = account
        self.password = password
        self.info = info
        self.id = "{0}{1}".format(random.randrange(1000000, 1999999), random.choice(['a', 'b', 'c']))

# Su dung linked list de luu cac user thay vi 1 mang

Users = LinkedList()

tung = { "name": "tung", "password":"123123", "age": 23, "role": "teacher" }
tien = { "name": "tien", "password":"123123", "age": 18, "role": "student" }
duck = { "name": "duck", "password":"123123", "age": 19, "role": "student" }

Users.Push(tung)
Users.Push(tien)
Users.Push(duck)

def findUser(username):
    userdata = None
    return userdata

def checking(username, password):
    result = None
    return result

def ViewProfile(user):
    system('cls')
    Manager(user)

def ChangePassword(user):
    pass

def Manager(user):
    print("1. Press [1] to view profile info")
    print("2. Press [2] to change password")
    print("3. Press [3] to log out")
    action = input("Enter action: ")
    if action == '1': ViewProfile(user)
    if action == '2': ChangePassword(user)
    if action == '3': Login()

def Login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Kiem tra xem username, password co ton tai trong database khong
    i = Users.FindUser(username, password)
    print(i)


def main():
    Login()

if __name__ == '__main__': main()