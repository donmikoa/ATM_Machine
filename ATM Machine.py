import getpass
import string
import os

#  Creating The List Of Users, Pin And Account Statement

users = ["user1", "user2", "user3"]
pins = ["1234", "2222", "3333"]
amounts = [1000, 2000, 3000]
count = 0

#  Using The While Loop To Check For The Presence Of Username Inputed

while True:
    user = input("\n ENTER USER NAME")
    user = user.lower()
    if user in users:
        if user == user[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print("----------------")
        print("****************")
        print("INVALID USERNAME")
        print("****************")
        print("----------------")

# Checking the validity of the pin entered
while count < 3:
    print("------------------")
    print("******************")
    pin = str(getpass.getpass("PLEASE ENTER YOUR PIN"))
    print("******************")
    print("------------------")
    if pin.isdigit():
        if user == "user1":
            if pin == pins[0]:
                break
            else:
                count += 1
                print("-----------")
                print("***********")
                print("INVALID PIN")
                print("***********")
                print("-----------")
                print()

        if user == "user2":
            if pin == pins[1]:
                break
            else:
                print("-----------")
                print("***********")
                print("INVALID PIN")
                print("***********")
                print("-----------")
                print()

        if user == "user3":
            if pin == pin[2]:
                break
            else:
                print("-----------")
                print("***********")
                print("INVALID PIN")
                print("***********")
                print("-----------")
                print()
    else:
        print("------------------------")
        print("************************")
        print("PIN CONSISTS OF 4 DIGITS")
        print("************************")
        print("------------------------")
        count += 1

# If The Pin Entered 3 Times Is Invalid
if count == 3:
    print("-----------------------------------")
    print("***********************************")
    print("3 UNSUCCESFUL PIN ATTEMPTS, EXITING")
    print("!!!!!YOUR CARD HAS BEEN LOCKED!!!!!")
    print("***********************************")
    print("-----------------------------------")
    exit()

print("-------------------------")
print("*************************")
print("LOGIN SUCCESSFUL, CONTINUE")
print("*************************")
print("-------------------------")
print()
print("--------------------------")
print("**************************")
print(str.capitalize(users[n]), "Welcome to ATM BANK")
print("**************************")
print("----------ATM SYSTEM-----------")
#  Creating The Menu
while True: #  os.system("clear")
    print("-------------------------------")
    print("*******************************")
    response = input(
        "SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) "
        "\nLodgement__(L)  \nChange PIN_(P)  "
        "\nQuit_______(Q) \n: ").lower()
    print("*******************************")
    print("-------------------------------")
    valid_responses = ["s", "w", "l", "p", "q"]











