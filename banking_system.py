accountList = []

def createAccount():
    account = {}
    account["accno"] = int(input("Enter your account number: "))
    account["balance"] = 0 
    account["name"] = input("Enter account holder's name: ")
    account["email"] = input("Enter account holder's email: ")

    address["landmark"] = input("Enter the landmark: ")
    address["city"] = input("Enter city: ")
    address["pincode"] = input("Enter pincode: ")
    address = {}
    account["address"] = address

    accountList.append(address)
    
createAccount()

def getAccountIndex(accno):
    indices =[i for i, account in enumerate(accountList) if account.get("accno") == accno]
    return indices[0]

