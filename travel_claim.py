import datetime
import FormatValues as FV

def calculate_travel_claim():
    print()
    # constants
    PER_DIEM = 85.00
    MILEAGE = 0.17
    PER_DIEM_RENT = 65.00
    MILEAGE_OVER = 0.04
    EXECUTIVE = 45.00
    HST_RATE = 0.15

    bonusDays = 0
    kiloBonus = 0
    execBonus = 0
    bonus = 0
    typeCar = ""
    typeClaim = ""
    EmpNum = ""

    # Continuation loop
    while True:

        # user inputs
        # Number of characters for characters
        while True:
            try:
                EmpNum = input("Enter the employee number:                           ")
            except:
                print("Employee number is invalid, please try again")
            if len(EmpNum) != 5:
                print("Employee numbers are usually 5 characters, please try again")
            else:
                break

        # This is a loop to validate the first name
        while True:
            CustFirsName = input("Enter the customer's first name:                     ").title()
            if CustFirsName == "":
                print("Customer name cannot be blank, try again")
            else:
                break

        # This is a loop to validate the last name
        while True:
            CustLasName = input("Enter the customer's last name:                      ").title()
            if CustLasName == "":
                print("Customer name cannot be blank, try again")
            else:
                break

       # This is a loop to validate the location of the trip
        while True:
            LocOfTrip = input("Enter the location of the trip:                      ")
            if LocOfTrip == "":
                print("Location of the trip cannot be blank, please try again")
            else:
                break

        # This is a loop to validate the Start Date
        while True:
            try:
                StartDate = input("Enter the start date of the trip(YYYY-MM-DD):        ")
                startDateObj = FV.ObjDate(StartDate)
            except:
                print("StartDate is invalid, please try again(YYYY-MM-DD)")
            else:
                break

        # This is a loop to validate the End Date
        while True:
            try:
                EndDate = input("Enter the end date of the trip(YYYY-MM-DD):          ")
                endDateObj = FV.ObjDate(EndDate)
            except:
                print("End Date is invalid, please try again(YYYY-MM-DD)")
            else:
                NumOfDays = (endDateObj - startDateObj).days
                if NumOfDays > 7:
                    print("End date cannot be longer than 7 days from start date, try again(YYYY-MM-DD)")
                elif NumOfDays > 3:
                    bonusDays += 100.00
                else:
                    break
            break

        # This is a loop to validate if they used their own car, or if a car was rented
        while True:
            CarType = input("Enter the car used, O for own and R for Rented(O/R): ").upper()
            if CarType == "":
                print("The car used cannot be blank, please try again(O/R)")
            elif CarType != "O" and CarType != "R":
                print("Car can only be owned or rented, please try again")
            elif CarType == "O":
                typeCar = "Own"
                while True:
                    try:
                        kiloUsed = int(input("Enter total kilometers driven: "))
                    except:
                        print("Kilometers is invalid, please try again")
                    else:
                        if kiloUsed > 2000:
                            print("Kilometers cannot exceed 2000, please try again")
                        elif kiloUsed > 1000:
                            kiloBonus += kiloUsed * (MILEAGE + MILEAGE_OVER)
                            break
                        else:
                            kiloBonus += kiloUsed * MILEAGE
                            break
                break
            elif CarType == "R":
                typeCar = "Rental"
                break

        # This is a loop to validate the claim type as standard or executive (S/E)
        while True:
            claimType = input("Standard claim or executive claim (S/E):             ").upper()
            if claimType == "":
                print("Claim type cannot be blank, please try again")
            elif claimType != "S" and claimType != "E":
                print("Claim type can only be S or E, please try again")
            elif claimType == "S":
                typeClaim = "Standard"
                break
            elif claimType == "E":
                typeClaim = "Executive"
                execBonus += NumOfDays * 45.00
                break

        # Calculations
        dec15Date = str(startDateObj.year) + "-12-15"
        dec15DateObj = datetime.datetime.strptime(dec15Date, "%Y-%m-%d")
        dec22Date = str(startDateObj.year) + "-12-22"
        dec22DateObj = datetime.datetime.strptime(dec22Date, "%Y-%m-%d")
        if dec15DateObj <= startDateObj <= dec22DateObj:
            bonus += NumOfDays * 50

        perDiemAmt = (NumOfDays * PER_DIEM)
        mileageAmt = kiloBonus
        bonusAmt = bonusDays + execBonus + bonus
        claimAmt = perDiemAmt + mileageAmt + bonusAmt
        HST = claimAmt * HST_RATE
        claimTotal = claimAmt + HST

        print()
        print("Employee Travel Claim Receipt")
        print("-----------------------------")
        print()
        print(f"Employee #: {EmpNum:>17s}")
        print(f"Employee: {CustFirsName + ' ' + CustLasName:>19s}")
        print()
        print(f"Location: {LocOfTrip:>19s}")
        print(f"Start Date: {StartDate:>17s}")
        print(f"Number of days: {NumOfDays:>13d}")
        print()
        print(f"Car type: {typeCar:>19s}")
        print(f"Claim Type: {typeClaim:>17s}")
        print()
        print(f"Per Diem: {'${:,.2f}'.format(perDiemAmt):>19s}")
        print(f"Mileage: {'${:,.2f}'.format(mileageAmt):>20s}")
        print(f"Bonus: {'${:,.2f}'.format(bonusAmt):>22s}")
        print("-----------------------------")
        print(f"Subtotal: {'${:,.2f}'.format(claimAmt):>19s}")
        print(f"HST: {'${:,.2f}'.format(HST):>24s}")
        print("-----------------------------")
        print(f"Total Expenses: {'${:,.2f}'.format(claimTotal):>13s}")
        print()

        cont = input("Would you like to calculate another expense? Yes or No?(Y/N)").upper()
        if cont != "Y":
            break

