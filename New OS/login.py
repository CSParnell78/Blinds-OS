import os, time
os.system("color 70")

login_user = open("user/username.pass")
login_pass = open("user/password.pass")

l_u = login_user.read()
l_p = login_pass.read()

pas = input("Please Enter Password To " + l_u + " To Login: ")

if pas == l_p:
    print("Opening Blinds-OS Home")
    time.sleep(0.5)
    with open("user/data.info", "w") as f:
        f.writelines("3")

    os.startfile("Blinds-OS.py")
else:
    print("Wrong Password To " + l_u)
    os.startfile("Blinds-OS.py")