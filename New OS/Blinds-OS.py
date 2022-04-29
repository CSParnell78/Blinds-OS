import os

data_info = open("user/data.info")
data = data_info.read()

if data == "0":
    os.startfile("register.py")
    print("Opening Register Page...")

if data == "1":
    os.startfile("login.py")
    print("Opening Login Page...")

if data == "3":
    os.startfile("Blinds-OS_Home.py")
    print("Opening Home Page...")

if data == "4":
    os.startfile("crash.py")


