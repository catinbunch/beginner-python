import random

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = random.choice(options)

while True:
    print("Guess a number 1-10 or exit to quit")
    userinput = input()
    #if userinput == "exit": break
    userinput=int(userinput)

    if value == userinput:
        print("You guessed right!") break
    elif value > userinput:
        print("guess is too low!")
    else: print("guess is too high!")
    #print ("Computer number:", value)
