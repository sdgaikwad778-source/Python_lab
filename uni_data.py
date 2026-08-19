accountList= []

#create account
def createAccount():
    account = {}
    account["accno"] = len(accountList)+1
    account["balance"] = 0
    account["name"]=input("enter your name:")
    account["email"]=input("enter your email:")
    account["password"]=input("enter your password:")
    address = {}
    address["landmark"] = input("enter landmark")
    address["city"] = input("enter city")
    address["country"] = input("enter country")
    address["state"] = input("state")
    address["picode"] = input("enter pincode")
    account["address"]=address
    accountList.append(account)
    
def getAccountIndex(accno):
    indices =[i for i, account in enumerate(accountList) if account.get("accno") == accno]
    return indices[0]

def deposit():
    accno = int(input("enter your account no :"))
    index = getAccountIndex(accno)
    amount = float(input("enter amount to deposite"))
    accountList[index]["balance"] = accountList[index]["balance"] + amount

def withdraw():
    accno = int(input("enter your account no :"))
    index = getAccountIndex(accno)
    amount = float(input("enter amount to withdraw"))
    accountList[index]["balance"] = accountList[index]["balance"] - amount

def checkbalance():
     accno = int(input("enter your account no :"))
     index = getAccountIndex(accno)
     print(accountList[index]["balance"])

createAccount()
deposit()
checkbalance()
withdraw()
checkbalance()