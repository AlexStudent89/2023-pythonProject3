import random

Number = random.randint(1, 27)
print(Number)


# Travel Claim Form info
EmpNum = input("Enter the employee number: ")
EmpFirName = input("Enter the employee first name: ")
EmpLasName = input("Enter the employee last name: ")
LocOfTrip = input("Enter the location of the trip: ")
StarDate = input("Enter the start date: ")
EndDate = input("Enter the end date: ")
NumDays = input("Enter the number of days (1-7): ")
TotKiloTrav = input("Enter the total kilometers traveled (S or E):")

# Continuation loop
while True:

    # Number of characters for characters
    while True:
        if EmpNum == "":
            print("Employee number cannot be blank, try again")
        elif len(EmpNum) != 5:
            print("Employee numbers are usually 5 characters, please try again")
        else:
            break

    # This is a loop to validate the first name
    while True:
        CustFirsName = input("Enter the customer's first name:   ").title()
        if CustFirsName == "":
            print("Customer name cannot be blank, try again")
        elif CustFirsName == "End":
            exit()
        else:
            break

    # This is a loop to validate the last name
    while True:
        CustLasName = input("Enter the customer's last name:    ").title()
        if CustLasName == "":
            print("Customer name cannot be blank, try again")
        else:
            break

    # This is a loop to validate the Start Date
    while True:
        StarDate = input("Enter the start date of the trip,:         ")
        if StarDate == "":
            print("StarDate cannot be blank, please try again")
        elif int(StarDate):
            print("The start date must be entered and valid, please try again")
        else:
            break