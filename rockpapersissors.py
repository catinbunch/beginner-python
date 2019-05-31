import random

while True:
    print("make input or type 'exit' to quit")
    a=random.randint(1, 3)
    uservar=input()
    if uservar=="exit": break
    i=0
    if uservar=="rock":
        i=1
    elif uservar=="paper":
        i=2
    elif uservar=="sissors":
        i=3
    else:
        print("wrong input")

    if a==i:
        print("tie")
    elif a==1:
        if i==2: print("user wins")
        if i==3: print("computer wins")
    elif a==2:
        if i==1: print("computer wins")
        if i==3: print("user wins")
    elif a==3:
        if i==1: print("user wins")
        if i==2: print("computer wins")
