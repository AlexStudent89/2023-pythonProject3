# Author: Alex Ewida, Mohamed Maghrebi, Manny Nwokedi
# Written: June 23, 2023
# Program that does something cool with strings and dates
import datetime
import re

# Strings and Dates

# Continuation loop
while True:

    # This is a loop to validate the employee’s first name
    while True:
        EmpFirsName = input("Enter the employee's first name:                              ").title()
        if EmpFirsName == "":
            print("Employee's first name cannot be blank, try again")
        elif EmpFirsName == "End":
            exit()
        else:
            break

    # This is a loop to validate the employee’s last name
    while True:
        EmpLasName = input("Enter the employee's last name:                               ").title()
        if EmpLasName == "":
            print("Employee's last name cannot be blank, try again")
        else:
            break

    # This is a loop to validate the employee’s phone number
    while True:
        PhoneNum = input("Enter the employee's phone number:                            ")
        if PhoneNum == "":
            print("Employee phone number cannot be blank, try again")
        elif len(PhoneNum) != 10:
            print("Phone numbers are usually 10 digits, please try again")
        else:
            break

    # This is a loop to validate the current date
    while True:
        CurrDate = input("Date: (YYYY-MM-DD):                                           ")
        if CurrDate == "":
            print("Current date cannot be blank, try again")
        else:
            break

    # This is a loop to validate how long they worked for the company
    while True:
        EmpWorkCom = input("Enter the amount of time the employee worked for the company: ")
        if EmpWorkCom == "":
            print("The amount of time the employee worked for the company cannot be blank, try again")
        else:
            break

    # This is a loop to validate the employee’s start date
    while True:
        EmpStartDate = input("Enter the employee’s start date(YYYY-MM-DD):                  ").title()
        if EmpStartDate == "":
            datetime.datetime.now()
            print("Employee start date cannot be blank, try again(YYYY-MM-DD)")
        else:
            break

    # This is a loop to validate the employee’s birthdate
    while True:
        EmpBirDate = input("Enter the employee’s birthdate(YYYY-MM-DD):                   ").title()
        if EmpBirDate == "":
            print("Employee start date cannot be blank, try again(YYYY-MM-DD)")
        else:
            break

    # This is a loop to validate how long till their birthday
    while True:
        HowTillEmpBirth = input("Enter how long till the employee's birthday:                  ")
        if HowTillEmpBirth == "":
            print("The amount of time till the employee's birthday cannot be blank, try again")
        elif HowTillEmpBirth == "End":
            exit()
        else:
            break

        Wait = input("Press ENTER to continue ...")