list = []
userlist = []
def addNewStudent(list):
    user = {} 
    user["rollno"] = int( input("Enter your rollno: "))
    user["name"] = input("Enter your name: ")
    user["marks"] = float(input("Enter your marks: "))
    address = {}
    print("Enter your address")
    address["landmark"] = input("Enter Landmark: ")
    address["city"] = input("Enter City: ")
    address["pincode"] = input("Enter Pincode: ")
    user["address"] = address
    list.append(user)
    
addNewStudent(list)
addNewStudent(userlist)
    
def printStudentList():
    for user in list:
    # print(user["name"]  + " " + str(user["rollno"]))
        print("My name is {} and rollno is {}.".format(user["name"], user["rollno"]))

def passedStudentList():
       for user in list:
           if(user["marks"]>=50):
                print("My name is {} and rollno is {}.".format(user["name"], user["rollno"]))
passedStudentList()

def printStudentByCity(city):
    for user in list:
        if(user["address"]["city"] == city):
            print("My name is {} and rollno is {}.".format(user["name"], user["rollno"]))
printStudentByCity("pune")