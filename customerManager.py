creatingClass

class CustomerManager():
    
    customerList = []
    
    def addNewCustomer(self, customer):
        self.customerList.append(customer)
        
cm = CustomerManager()

class Customer:

    def __init__(self,name, email, password):
        
        self.name = name
        self.email = email
        self.password = password

    def printDetails(self):
        print("Customer Name: ", self.name)
        print("Cutsomer Email: ", self.email)
        
    def resetPassword(self,password):
        self.password = password
        print("New Password: ", self.password)
        
    def getEmail(self):
        return self.email
c1 = Customer("Santosh", "sdgaikwad", 12345)
#adding new cutsomer
c2 = Customer("Ian", "Ian7@79", 13468)
# print(c2)
# print(c1.name)
# print(c1.email)
# print(c1.password)
# c1.printDetails()
# c2.printDetails()
# c2.resetPassword(12345)
#c1.resetPassword(12345)

print(c1.getEmail())