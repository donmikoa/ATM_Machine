import getpass
import string
import os

#  Creating The List Of Users, Pin And Account Statement

users = ["user", "user2", "user3"]
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
