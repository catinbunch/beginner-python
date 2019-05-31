#loops and conditionlas
"""
a=input()
a=int(a) #chnaging user input from string to int so can compare to 0
if a>0 :
    print("positive number")
else:
    print("negative number")


# underscore means drop
b=0
for _ in range(10): #automalically goes from 0 10 9, to do counting by 2s or 3s etc would do rang(10,x) x being what you want to count by
    b+=1 #loop that runs 10 times and incrments b by one each time
    print(b)

#list operations
#creating and adding
somelist=[] #way to create an array or list
for i in range(20):
    if i%2==0:
        somelist.append(i) #way to add to a list
    else:
        somelist.append("ODD")

#print(somelist[3]) #printing 4th element -1 is always the last element, defulat value of pop

#removing
c=somelist.pop() #pop is removing the last element off a list and assigning it to that variable
print(c)
print(somelist)
#for removing elemts from the end
for i in range(5):
    somelist.pop()
print(somelist)


def new_function():
    new=[]
    for i in range(20):
        new.append(i)
    return new #returing a list out of a function

f= new_function()
print(f)
#print(len(f))#return length of the list

for x in f:
    print(x)


#while loops
a=0
while a < 10:
    a+=1
print(a)

#infident loop and breaking it
while True:
    a+=1
    print("here")
    if a==20: break
"""
b="hey"
for _ in range(10):
    b+='y' #adding onto the end of a string
    if b=="heyyy": #comparing strings
        print("success")
print(b[0])
