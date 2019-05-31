while True:
    age = input("How old are you? or exit to quit ")
    if age=="exit": break
    age=int(age)
    if age >= 17:
        print("can see a rated R movie")
    elif age < 17 and age > 12:
        print("can see a rated PG-13 movie")
    else:
        print("can only see rated PG movies")
