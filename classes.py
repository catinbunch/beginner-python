class Hello(object): #start with capital letter var
    def __init__(self,name,age,sex): #start with this, pass it itself and any other pramaters
        self.name=name
        self.age=age
        self.sex=sex

    def minusyear(self, num):
        self.age = self.age - num;

print("Name?")
tempname=input()
print("Age?")
tempage=int(input())
print("Sex?")
tempsex=input()

#user1=Hello(tempname,tempage,tempsex)
#print(user1.name,user1.age,user1.sex)

list1=[]
list1.append(Hello(tempname,tempage,tempsex))
print(list1[0].name,list1[0].age,list1[0].sex)

list1[0].minusyear(10)
print(list1[0].age)
