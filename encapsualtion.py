class Student:
    def __init__(self):
        self.name = "santosh"
        
student1 = Student()

userlist = []
user = {}

# user["keyname"] = "value1"
# user["keyname"] = "value2"
# userlist.append(user)
# #user(key-value added to the userlist)

user["name"] = input("Enter your name: ")

userlist.append(user)

print(userlist)

class Student:
    def __init__(self):
        self.name = "Santosh"
student1 = Student()
print(student1.name)        

class Student:
    def __init__(self):
        self.__name = "santosh"
        self.__marks= 90
student1 = Student()
print(student1.__marks)
print(student1.__name)

# so, how do we access that marks. 
# We create a method that gives us controlled access.

class AutoMobiles():
    def __init__(self):
        self.__name = "mahindra"
        self.__price = 200000

    def get_module(self):
        return self.__name, self.__price
    
model =  AutoMobiles()
print(model.get_module())

class Student():
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        print("My name is: ", self.name)
        
student1 = Student("Santosh")
student1.introduce()


class Office:
    def __init__(self, sales):
        self.__sales = sales
        
    def get_sales_num(self):
        return self.__sales

first_quater = Office(500000)   
print(first_quater.get_sales_num)

    
