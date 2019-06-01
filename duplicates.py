one = ["hey", "hi", "i am", "hey", "hi"]
temp = []

for val in one:
    if val in temp: #way to check if an element , can also val not in
        pass
    else:
        temp.append(val)

print (temp)
