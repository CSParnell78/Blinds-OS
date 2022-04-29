import os, time
import sys

print("""Welcome To ComScreen [1.00] 
If you need help for commands type help""")
print()

while True:
    command = input("Command >> ")
    os.system(command)

    if command == "cms":
        os.startfile("command.py")
        sys.exit()

    if command == "help":
        print("Custom Commands Are Below")
        print("cms - Runs a new window of ComScreen")