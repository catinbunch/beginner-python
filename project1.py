#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

y=input()
y=int(y) #ALWAYS REMEBER TO CHNAGE TO INT
a=[1,2,3,30,60,70,80,-5,7,-900]
newlist=[]

for x in range(len(a)):
    if a[x] > y:
        newlist.append(a[x])

print(newlist)
