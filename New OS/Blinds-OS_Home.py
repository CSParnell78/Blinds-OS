import os
import socket
import time
import sys

os.system("color 70")

login_user = open("user/username.pass")
login_pass = open("user/password.pass")
l_u = login_user.read()
l_p = login_pass.read()

with open("user/data.info","w") as f:
    f.writelines("1")

print("Welcome " + l_u + " To Blinds-OS Home")
print("The Time is " + time.strftime("%H:%M"))
print("OS Repository - ")

print("""You Can
1. Comand Prompt 
2. Calculator
3. System Configuration
4. Games
5. Safe Shutdown""")

choose = input("[?]: ")

if choose == "1":
    os.startfile("Blinds-OS_Home.py")
    os.startfile("command.py")

if choose == "2":
    os.startfile("Blinds-OS_Home.py")
    os.startfile("calc.py")

if choose == "3":
    os.startfile('Blinds-OS_Home.py')
    os.startfile('sysconfig.py')


if choose == "4":
    os.startfile("Blinds-OS_Home.py")
    os.startfile("games.py")

if choose == "5":
    print("Closing Blinds...")
    time.sleep(2)
    sys.exit()
