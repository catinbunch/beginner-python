import random

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    print("Guess a number 1-10 or exit to quit")
    userinput = input()
    if userinput == "exit": break
    userinput=int(userinput)
    value = random.choice(options)

    if value == userinput:
        print("You guessed right!")
    elif value > userinput:
        print("guess is too low!")
    else: print("guess is too high!")
    print ("Computer number:", value)
