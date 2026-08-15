class Student:
    pass
#creating first object
student1 = Student()
student1.name = "Santosh"
student1.email = "santosh@123gmail.com"

print(student1.name)
print(student1.email)

class Car:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
car1 = Car("Mahindra", 2000000)