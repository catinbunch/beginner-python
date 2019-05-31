import random

array = ["U", "L", "N", "C"]

upperlist = "ABCDEFGHIJKLMNOPQRSTUV"
lowerlist = "abcdefghijklmnopqrstuvwxyz"
numberlist = "1234567890"
charlist = "!@#$%&*"

def makepassword(num):
    password = ''
    for i in range(0,num):
        new = random.choice(array)
        if new == "U":
            password+=random.choice(upperlist)
        elif new == "L":
            password+=random.choice(lowerlist)
        elif new == "N":
            password+=random.choice(numberlist)
        elif new == "C":
            password+=random.choice(charlist)
    return password

print("input password length")
num = int(input())
final = makepassword(num)
print("Gnerated password:\n", final)
