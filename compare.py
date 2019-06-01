import time

l1 = [3, 4, 5, 6, 7, 8, 9, 0, 2, 4, 5, 33]
l2 = [3, 5, 6, 8, 23, 65, 33]
matches = []

length1=len(l1)
length2=len(l2)


z = 0

for i in range(0, length1):
    for j in range(0,length2):
        if l2[j] == l1[i]:
            matches.append(l2[j])

print(matches)

#cooler solution "pythonic way"s
start = time.time() #how to calculate time it takes to run
for val in l1: #this for loops iterates through the whole list and val = each value
    if val in l2: #checks if the val is in the list
        matches.append(val)
print("Time:", time.time()-start)


#one line solution, fastest one
matches = [val for val in l1 if val in l2] #function that creates list
print("Time:", time.time()-start)
