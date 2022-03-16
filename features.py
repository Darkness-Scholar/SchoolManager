import random

def isExistedUser(username):  # check if user is already registered
    result = False
    readFile = open("users.txt", "r")
    for line in readFile:
        udata = line.replace("\n", "").split(";")
        if udata[0] == username:
            result = True
            break
    readFile.close()
    return result


def Register():
    username = input("Enter username: ")
    existed = isExistedUser(username)
    if existed == True:
        print("User already registered, Re try: ")
        Register()
    if existed == False:
        fullname = input("Enter fullname: ")
        password = input("Enter password: ")
        birth = input("Enter birth day: (example 18/02/1999) ")
        id = str(random.randrange(1000000, 1999999)) + str(random.choice(['a', 'b', 'c', 'd', 'e', 'f']))
        temp = "\n{0};{1};{2};{3};{4};student".format(username, fullname, password, birth, id)
        writeFile = open("users.txt", "a")
        writeFile.write(temp)
        writeFile.close()
