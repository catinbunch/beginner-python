print("Hello World") #print statement

a=10
b="hey"
c=8.4
d="you"

def new_func(var): #way to create a function
    newvar=var*7
    return newvar

e=new_func(c) #calling function
print(e)
print(b+' '+d) #adding together 2 strings
#getting user input
uservar=input() #user inputs are always strings
print(uservar)
print(type(c)) #returns the class that the variable belongs too
