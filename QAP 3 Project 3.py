# Author: Alex Ewida
# Written: June 14, 2023
# Program to test true loops and calculations
import datetime
import re

# Constants
LICENCE_FEE_5K = 75.00
LICENCE_ABOVE_5K = 165.00
TRANSFER_FEE_LOWER = 0.01
TRANSFER_FEE_ABOVE = 0.026
HST_RATE = 0.15
CurDate = datetime.datetime.now()
InvoiceDate = (CurDate.strftime("%B %d, %Y"))
InvoiceDate2 = (CurDate.strftime("%d-%b-%y")).upper()
FirstPayDate = (CurDate+datetime.timedelta(days=30))
FirstPayDate = FirstPayDate.strftime("%d-%b-%y").upper()

# Continuation loop
while True:

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

    # This is a loop to validate the phone number
    while True:
        PhoneNum = input("Enter the customer's phone number: ")
        if PhoneNum == "":
            print("Customer phone number cannot be blank, try again")
        elif len(PhoneNum) != 10:
            print("Phone numbers are usually 10 digits, please try again")
        else:
            break

    # This is a loop to validate the plate number
    while True:
        PlatNum = input("Enter the plate number:            ")
        if PlatNum == "":
            print("Customer's car plate number cannot be blank, try again")
        elif len(PlatNum) != 6:
            print("Plate numbers are usually 3 letters and 3 numbers")
        elif not re.match(r'^[A-Z]{3}\d{3}$', PlatNum):
            print("Plate numbers are usually 3 letters and 3 numbers")
        else:
            break

    # This is a loop to validate the make of the car
    while True:
        CarMake = input("Enter the make of the car:         ")
        if CarMake == "":
            print("Customer's car make cannot be blank, try again")
        else:
            break

    # This is a loop to validate the model of the car
    while True:
        CarMod = input("Enter the car model:               ")
        if CarMod == "":
            print("Customer's car model cannot be blank, try again")
        else:
            break

    # This is a loop to validate the year of the car
    while True:
        CarYear = input("Enter the year of the car:         ")
        if CarYear == "":
            print("Customer's car year cannot be blank, please try again")
        elif len(CarYear) != 4:
            print("The year of the car are usually 4 digits, please try again")
        else:
            break

    # This is a loop to validate the selling price of the car
    while True:
        SalePrice = int(input("Enter the car's selling price:     "))
        if SalePrice == "":
            print("Car sale price cannot be blank, please try again")
        elif SalePrice > 50000.00:
            print("Sale price cannot exceed $50000.00")
        else:
            break

    # This is a loop to validate the trade in
    while True:
        AmnOfTrad = int(input("Enter the amount of the trade in:  "))
        if AmnOfTrad == "":
            print("The amount of trade in must not be blank, please try again")
        elif AmnOfTrad > SalePrice:
            print("The amount of trade in cannot exceed $50000.00")
        else:
            break

    # This is a loop to validate the salespersons name
    while True:
        SalePerNam = input("Enter the salespersons name:       ").title()
        if SalePerNam == "":
            print("The salespersons name must not be blank, please try again")
        else:
            break

    # Calculations
    PriceAfterTrade = SalePrice - AmnOfTrad
    if SalePrice <= 5000:
        LicFee = LICENCE_FEE_5K
    else:
        LicFee = LICENCE_ABOVE_5K
    if SalePrice < 20000:
        TrFee = TRANSFER_FEE_LOWER
    else:
        TrFee = TRANSFER_FEE_ABOVE
    fee2lic = LicFee
    fee2trans = TrFee
    SubTotal = PriceAfterTrade + fee2lic + fee2trans
    HST = SubTotal * HST_RATE
    TotalSalePrice = SubTotal + HST


    ReceiptNo = "23-765-9123"

    # This is my output or receipt
    print()
    print(f"Honest Harry Car Sales                        Invoice Date: {InvoiceDate}")
    print(f"Used Car Sale and Receipt                     Receipt No:   {ReceiptNo}")
    print()
    print(f"                                          Sale price:                ${'{:,.2f}'.format(SalePrice):>9s}")
    print(f"Sold to:                                  Trade Allowance:           ${'{:,.2f}'.format(AmnOfTrad):>9s}")
    print("                                          -------------------------------------")
    print(f"      {CustFirsName[0]}. {CustLasName:<29s}    Price after Trade:         ${'{:,.2f}'.format(PriceAfterTrade):>9s}")
    print(f"      125 Blackmarsh Rd                   License Fee:               ${'{:,.2f}'.format(LicFee):>9s}")
    print(f"      Paradise, NL A1A 1A1                Transfer Fee:              ${'{:,.2f}'.format(TrFee):>9s}")
    print("                                          -------------------------------------")
    print(f"Car Details:                              Subtotal:                  ${'{:,.2f}'.format(SubTotal):>9s}")
    print(f"                                          HST:                       ${'{:,.2f}'.format(HST):>9s}")
    print(f"{CarYear:>10s} {CarMake:<14s} {CarMod:<14s}  -------------------------------------")
    print(f"                                          Total sales price:         ${'{:,.2f}'.format(TotalSalePrice):>9s}")
    print("-------------------------------------------------------------------------------")
    print("                  Best used cars at the best prices!")

    print()
    print((" "*29), "Financing     Total       Monthly")
    print("    # Years    # Payments        Fee        Price       Payment")
    print("    -----------------------------------------------------------")

    # This is a loop to calculate the data 4 times
    for i in range(1, 5):
        NumPay = i * 12
        FinFee = 39.99 * i
        TotalPrice = TotalSalePrice + FinFee
        MonPay = TotalPrice/NumPay
        print(f"        {i}           {NumPay}       ${'{:,.2f}'.format(FinFee):>7s}    ${'{:,.2f}'.format(TotalPrice):>9s}    ${'{:,.2f}'.format(MonPay):>7s}")
    print("    -----------------------------------------------------------")
    print(f"    Invoice Date: {InvoiceDate2}       First Payment Date: {FirstPayDate}")