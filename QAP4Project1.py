# The One Stop Insurance Company

import datetime
import time
import FormatValues as FV
import re

def main():
    while True:
        try:
            with open("OSICDef.dat", "r") as file:
                policy_number = int(file.readline())
                basic_premium = float(file.readline())
                discount_additional_cars = float(file.readline())
                extra_liability_cost = float(file.readline())
                glass_coverage_cost = float(file.readline())
                loaner_car_cost = float(file.readline())
                hst_rate = float(file.readline())
                processing_fee = float(file.readline())
        except:
            print("OSICDef.dat does not exist.")
            exit()
        else:
            print()
            print("OSICDef.dat exists.")
            break

    while True:
        while True:
            first_name = input("Enter customer's first name: ").title()
            if first_name.isalpha():
                break
            else:
                print("Invalid first name. Please enter a valid first name.")
        while True:
            last_name = input("Enter customer's last name: ").title()
            if last_name.isalpha():
                break
            else:
                print("Invalid last name. Please enter a valid last name.")
        while True:
            address = input("Enter customer's address: ")
            if address == "":
                print("Invalid address. Please enter a valid address.")
            else:
                break
        while True:
            city = input("Enter customer's city: ").title()
            if city.isalpha():
                break
            else:
                print("Invalid city. Please enter a valid city.")
        ProvList = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
        while True:
            province = input("Enter customer's province (2-letter code): ").upper()
            if province in ProvList:
                break
            else:
                print("Invalid province code. Please enter a valid 2-letter code.")
        while True:
            postal_code = input("Enter a Canadian postal code (e.g., A1A 1A1): ")
            pattern = r"^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$"
            if re.match(pattern, postal_code):
                print(f"Valid postal code: {postal_code}")
                break
            print("Invalid postal code. Please enter a valid Canadian postal code.")
        while True:
            phone_number = input("Enter customer's phone number: ")
            if phone_number.isdigit() and len(phone_number) == 10:
                break
            else:
                print("Invalid phone number. Please enter a valid phone number.")
        while True:
            NumCars = int(input("Enter number of cars being insured: "))
            if NumCars <= 0:
                print("Invalid number of cars. Please enter a valid number of cars.")
            else:
                break
        while True:
            ExLiabFee = 0
            ExLiability = input("Enter extra liability up to $1,000,000 (Y)es or (N)o: ").upper()
            if ExLiability == "":
                print("Invalid extra liability. Please enter a Y or N.")
            elif ExLiability == "Y":
                ExLiabFee += extra_liability_cost * int(NumCars)
                break
            else:
                break
        while True:
            GLCovFee = 0
            GlassCoverage = input("Accept glass coverage (Y)es or (N)o: ").upper()
            if GlassCoverage == "":
                print("Invalid glass coverage. Please enter a Y or N.")
            elif GlassCoverage == "Y":
                GLCovFee += glass_coverage_cost * int(NumCars)
                break
            else:
                break
        while True:
            LCovFee = 0
            LoanerCar = input("Accept loaner car insurance (Y)es or (N)o: ").upper()
            if LoanerCar == "":
                print("Invalid loaner car. Please enter a Y or N.")
            elif LoanerCar == "Y":
                LCovFee += loaner_car_cost * int(NumCars)
                break
            else:
                break
        while True:
            PaymentType = input("Payment in (F)ull or (M)onthly: ").upper()
            if PaymentType == "":
                print("Invalid payment type. Please enter a F or M.")
            elif PaymentType == "F":
                payments = 1
                break
            elif PaymentType == "M":
                payments = 8
                break

        #Calculations
        insurancePremium = basic_premium + (NumCars - 1) * (basic_premium * discount_additional_cars)
        TotExtCharge = ExLiabFee + GLCovFee + LCovFee
        TotInsurancePremium = insurancePremium + TotExtCharge
        TotHST = TotInsurancePremium * hst_rate
        TotCustomerCharge = TotInsurancePremium + TotHST
        invoiceDateObj = datetime.date.today()
        if payments == 8:
            MonPayment = round((TotCustomerCharge + processing_fee) / payments, 2)
            if invoiceDateObj == 12:
                NextPaymentDue = datetime.date(invoiceDateObj.year + 1, 1, 1)
            else:
                NextPaymentDue = datetime.date(invoiceDateObj.year, invoiceDateObj.month + 1, 1)

        print()
        print("The One Stop Insurance Company")
        print("Customer Insurance Receipt")
        print("__________________________________")
        print(f"Customer: {first_name:>17s}, {last_name:<14s}")
        print(f"Address: {address:>25s}")
        print(f"City: {city:>28s}")
        print(f"Province: {province:>24s}")
        print(f"Postal Code: {postal_code:>21s}")
        print(f"Phone: {phone_number:>27s}")
        print(f"Number of Cars: {NumCars:>18d}")
        print(f"Insurance Base Premium: {FV.FDollar2(basic_premium):>10s}")
        if ExLiabFee <= 0:
            print("Extra Liability Declined")
        if ExLiabFee:
            print(f"Extra Liability Amount: {FV.FDollar2(ExLiabFee):>10s}")
        if GLCovFee <= 0:
            print("Glass Coverage Declined")
        if GLCovFee:
            print(f"Glass Coverage Amount: {FV.FDollar2(GLCovFee):>11s}")
        if LCovFee == 0:
            print("Loaner Car Declined")
        if LCovFee:
            print(f"Loaner Car Amount: {FV.FDollar2(LCovFee):>15s}")
        print(f"Insurance Premium: {FV.FDollar2(insurancePremium):>15s}")
        print(f"Total Ext. Charges: {FV.FDollar2(TotExtCharge):>14s}")
        print(f"Total Insurance Premium: {FV.FDollar2(TotInsurancePremium):>4s}")
        print(f"Total HST: {FV.FDollar2(TotHST):>23s}")
        print()
        print(f"Total Customer Charge: {FV.FDollar2(TotCustomerCharge):>11s}")
        if PaymentType == "M":
            print()
            print("Monthly Payment Plan")
            print("Processing Fee:", processing_fee)
            print("Monthly Payment:", MonPayment)
            print("Next Payment Due:", NextPaymentDue)
        print("__________________________________")

        with open("Policies.dat", "a") as file:
            file.write(str(first_name) + "\n")
            file.write(str(last_name) + "\n")
            file.write(str(address) + "\n")
            file.write(str(city) + "\n")
            file.write(str(province) + "\n")
            file.write(str(postal_code) + "\n")
            file.write(str(phone_number) + "\n")
            file.write(str(NumCars) + "\n")
            file.write(str(basic_premium) + "\n")
            file.write(str(discount_additional_cars) + "\n")
            file.write(str(extra_liability_cost) + "\n")
            file.write(str(glass_coverage_cost) + "\n")
            file.write(str(loaner_car_cost) + "\n")
            file.write(str(hst_rate) + "\n")
            file.write(str(processing_fee) + "\n")
            file.write(str(insurancePremium) + "\n")
            file.write(str(TotExtCharge) + "\n")
            file.write(str(TotInsurancePremium) + "\n")
            file.write(str(TotHST) + "\n")

        policy_number += 1
        cont = input("Continue?           (Y)es or (N)o: ").upper()
        if cont != "Y":
            with open("OSICDef.dat", "w") as file:
                file.write(str(policy_number) + "\n")
                file.write(str(basic_premium) + "\n")
                file.write(str(discount_additional_cars) + "\n")
                file.write(str(extra_liability_cost) + "\n")
                file.write(str(glass_coverage_cost) + "\n")
                file.write(str(loaner_car_cost) + "\n")
                file.write(str(hst_rate) + "\n")
                file.write(str(processing_fee) + "\n")
                file.write(str(insurancePremium) + "\n")
                file.write(str(TotExtCharge) + "\n")
                file.write(str(TotInsurancePremium) + "\n")
                file.write(str(TotHST) + "\n")
                exit()
        else:
            print("Let's process another policy.")

main()

