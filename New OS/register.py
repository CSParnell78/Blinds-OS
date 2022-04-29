import os, time
os.system("color 70")

username = input("Enter Your Desired Username: ")
email = input("Enter Your Email: ")
fPass = input("Enter Your Desired Password: ")
sPass = input("Enter Your Password Again: ")

if sPass == fPass:
    next = input("Press ENTER to finish setup")

    with open("user/data.info", "w") as f:
        f.writelines("1")
else:
    print("Wrong Password Try Again!")
    time.sleep(1)
    os.startfile("register.py")

with open("user/username.pass", "w") as f:
    f.writelines(username)

with open("user/password.pass", "w") as f:
    f.writelines(fPass)

os.startfile("Blinds-OS.py")