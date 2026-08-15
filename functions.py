#basics
def sayHello():
    print("hello")
sayHello()

#function with paramter
#I'll give you different names, just add greeting

def sayNamaste(name):#This name is paramter
    print(name,"Namaste")
sayNamaste("vivek")#This vivek input is arugment

#Parameter = variable waiting for a value
#Argument = actual value you give

#addition ex:
def add(a,b):
    print(a+b)
add(1,2)

#using return - it is more useful because it stores the value instead of just printing it
def sum(a,b):
    return a + b
result = sum(10,20)
print(result)

#functions with user input 
def user_input():
    name = input("Enter your name: ")
    return name
result = user_input()
print(result)

#multiple values stored

def mul_values(a,b):
    return a + b, a - b
add,sub = mul_values(10,20)
print(add)
print(sub)
    