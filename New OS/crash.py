import os, time

os.system('color 17')

print("Your Computer Has Crashed Because of a data overload")

print("Restarting in 5")
time.sleep(1)
os.system('cls')

print("Your Computer Has Crashed Because of a data overload")

print("Restarting in 4")
time.sleep(1)
os.system('cls')

print("Your Computer Has Crashed Because of a data overload")

print("Restarting in 3")
time.sleep(1)
os.system('cls')

print("Your Computer Has Crashed Because of a data overload")

print("Restarting in 2")
time.sleep(1)
os.system('cls')

print("Your Computer Has Crashed Because of a data overload")

print("Restarting in 1")
time.sleep(1)

with open("user/data.info", "w") as f:
    f.writelines("1")
    os.startfile("Blinds-OS.py")