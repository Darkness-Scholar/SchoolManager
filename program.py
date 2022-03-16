
import os
from os import system
from features import *
from llist import *
import time

Users = LinkedList()

def LoadData():
    readFile = open("users.txt", "r")
    for line in readFile:
        udata = line.replace("\n", "").split(";")
        temp = {
            "username": udata[0], 
            "fullname": udata[1], 
            "password": udata[2], 
            "birthday": udata[3],
            "id": udata[4],
            "role": udata[5]
        }
        Users.Push(temp)
    readFile.close()

LoadData()

def ViewProfile(user):
    i, userdata = Users.FindUser(user['username'], user['password'])
    print(userdata)
    print("Return to main menu after 3 seconds...")
    time.sleep(3)
    system('cls')
    Manager(user, i)

def ChangePassword(user, uid):
    newPassword = input('Enter new password: ')
    Users.SetPassword(uid, newPassword)
    print('Password changed, new result: ')
    # rewrite to data base file and reload, đây coi như bài tập cho các bạn
    ViewProfile(user)

def Logout():
    system('cls')
    print('Log out...')
    time.sleep(2)
    print('Log out...')
    Login()

def CreateSchoolYear():
    schoolYear = input("Enter School year: ")
    # create a new school year file
    createdDirectory = schoolYear

    dirName = 'tempDir'

    try:
        os.mkdir(createdDirectory)
        print("Directory " , createdDirectory , " Created ") 
    except FileExistsError:
        print("Directory " , createdDirectory ,  " already exists")

    i = input("Press [1] to create class")
    if (i == '1'): CreateClass(schoolYear)

def CreateClass(schoolYear):
    className = input("Enter class name: ")
    # create class file in school year directory
    createdFile = schoolYear+"/"+className+".txt"
    file = open(createdFile, "w")
    file.close()
    action = input("Press [y] to continue create, or exit")
    if action == "y": CreateClass(schoolYear)
    
def AddNewStudent():
    schoolYear = input("Enter school year: ") # năm học nào
    className = input("Enter class name: ") # lớp nào
    dirname = schoolYear+"/"+className+".txt"
    file = open(dirname, "a")
    username = input("Enter username: ")
    uid, user = Users.FindByUserName(username)
    temp = "name:{};id:{};age:{}".format(user['username'], uid, user['age'])
    file.write(temp)

    file.close()


def AddNewStudentByFile():
    inputFile = "students.txt"
    schoolYear = input("Enter school year: ") # năm học nào
    className = input("Enter class name: ") # lớp nào
    dirname = schoolYear+"/"+className+".txt"

    readFile = open(inputFile, "r")
    
    for line in readFile:
        uid, user = Users.FindByUserName(line.replace('\n', ''))
        print("Found :",line, uid)
        if uid == None: continue
        temp = "name:{};id:{};age:{}\n".format(user['username'], uid, user['age'])
        writeFile = open(dirname, "a")
        writeFile.write(temp)
        writeFile.close()

    readFile.close()
 
def Manager(user, uid):
    print("1. Press [1] to view profile info")
    print("2. Press [2] to change password")
    print("3. Press [3] to log out")

    if user['role'] == "teacher":
        print("4. Press [4] to create a school year")
        print("5. Press [5] to add students to class")
        print("6. Press [6] to add students by file")

    action = input("Enter action: ")
    if action == '1': ViewProfile(user)
    if action == '2': ChangePassword(user, uid)
    if action == '3': Logout()
    if user['role'] == "teacher":
        if action == '4': CreateSchoolYear()
        if action == '5': AddNewStudent()
        if action == "6": AddNewStudentByFile()

def Login():
    username = "tungxm123" #input("Enter username: ")
    password = "123123" #input("Enter password: ")

    # Kiem tra xem username, password co ton tai trong database khong
    # FindUser return ve 2 gia tri
    
    i, userdata = Users.FindUser(username, password)
    if userdata: 
        print("Dang nhap thanh cong")
        Manager(userdata, i)
        # Chay ham Manager
    else: 
        print("Dang nhap that bai")
        print(userdata)
        # Dang nhap lai (chay lai ham Login)
        Login()

def main():
    action = input("[1:LOGIN]  [2:REGISTER]\t")
    if action == "1": Login()
    if action == "2": Register()

if __name__ == '__main__': main()