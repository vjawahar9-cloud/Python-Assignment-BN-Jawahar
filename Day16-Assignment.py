
##1.withdraw limit exception

class withdrawerror(Exception):
    pass

try:
    balance=5000

    withdraw=int(input("Enter the withdraw amount"))
    
    if withdraw > balance:
        raise withdrawerror ("Error withdrawl amount")
    
    balance = balance - withdraw

    print("withdrawl successfull")

    print("Remaining balance",balance)

except withdrawerror as we:
    print("withdrawerror: ",we)





##2. Negative number exception

class negativenumbererror(Exception):
    pass

try:
    number = int(input("Enter the number"))

    if number < 0:
        raise negativenumbererror ("negative numbers are not allowed")

    print("positive numbers are allowed")

except negativenumbererror as nne:
    print("negativenumbererror: ", nne)
