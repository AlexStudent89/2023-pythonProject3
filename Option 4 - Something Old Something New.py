# Author: Alex Ewida, Mohamed Maghrebi, Manny Nwokedi
# Written: June 23, 2023
# Program about renting a book at a library
import datetime
import re

# Library name
LibName = input("Enter the name of the library:              ")

# Continuation loop
while True:

    # This is a loop to validate the Client's first name
    while True:
        CliFirName = input("Enter the client's first Name:              ").title()
        if CliFirName == "":
            print("The client's first Name cannot be blank, try again")
        elif CliFirName == "End":
            exit()
        else:
            break

    # This is a loop to validate the Client's last name
    while True:
        CliLasName = input("Enter the client's last name:               ").title()
        if CliLasName == "":
            print("The client's last name cannot be blank, try again")
        else:
            break

    # This is a loop to validate the client's phone number
    while True:
        PhoneNum = input("Enter the client's phone number:            ")
        if PhoneNum == "":
            print("Client phone number cannot be blank, try again")
        elif len(PhoneNum) != 10:
            print("Phone numbers are usually 10 digits, please try again")
        else:
            break

    # This is a loop to validate the client's library card number
    while True:
        LibCardNum = input("Enter the client's library card number:     ")
        if LibCardNum == "":
            print("Client library card number cannot be blank, try again")
        elif len(LibCardNum) != 15:
            print("Library card numbers are usually 15 digits, please try again")
        else:
            break

    # This is a loop to validate the rent date
    while True:
        RenDate = input("Enter the client's Rent Date (YYYY-MM-DD):  ")
        if RenDate == "":
            print("Rent date cannot be blank, try again")
        else:
            break

    # This is a loop to validate the client's return date
    while True:
        CliRetDate = input("Enter the client's return date (YYYY-MM-DD):")
        if CliRetDate == "":
            print("Client's return date cannot be blank, try again")
        else:
            break

    # This is a loop to validate the client's birthdate
    while True:
        CliBirDate = input("Enter the client's birthdate (YYYY-MM-DD):  ").title()
        if CliBirDate == "":
            print("Client's birthdate cannot be blank, try again")
        else:
            break

    # This is a loop to validate the client's address
    while True:
        ClientAdd = input("Enter the client's address:                 ").title()
        if ClientAdd == "":
            print("Client's address cannot be blank, try again")
        else:
            break

    # This is a loop to validate the expiration date of card
    while True:
        ExpDate = input("Enter the expiration date:                  ")
        if ExpDate == "":
            print("Card expiration date cannot be blank, try again")
        else:
            break

    # This is a loop to validate the book title
    while True:
        BookTitle = input("Enter the book title:                       ").title()
        if BookTitle == "":
            print("Book title cannot be blank, try again")
        else:
            break

    # This is a loop to validate the book author
    while True:
        BookAuth = input("Enter the book author name:                 ").title()
        if BookAuth == "":
            print("Book author name cannot be blank, try again")
        else:
            break

        Wait = input("Press ENTER to continue ...")