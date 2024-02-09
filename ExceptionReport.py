# Monthly Payment Listing for the One Stop Insurance Company
# Written by Alex Ewida
# Written on August 1, 2023
import csv
import datetime
import FormatValues as FV

Cost = 234.8968

print(f"Total cost:       {FV.FDollar2(Cost):>9s}")

#Constants
EXTRA_LIABILITY = 130
GLASS_COVERAGE = 86
LOANER_CAR_OPTION = 58
HST_RATE = .15
MONTHLY_PAYMENT = 39.99

print("ONE STOP INSURANCE COMPANY")
print("MONTHLY PAYMENT LISTING AS OF dd-Mon-yy")
print()
print("POLICY CUSTOMER                 TOTAL                 TOTAL       MONTHLY")
print("NUMBER NAME                    PREMIUM      HST       COST        PAYMENT")

print("=" * 73)

TotalPolicies = 0
TotalSubtotal = 0
TotalHST = 0
TotalPremium = 0
TotalMonthlyPayment = 0

with open("PoliciesData.dat", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header line

    for policy in reader:
        PolNum = policy[0].strip()
        PolicyDate = policy[1].strip()
        CustFirstName = policy[2].strip()
        CustLastName = policy[3].strip()
        NumCars = int(policy[9].strip())
        OptLiability = policy[10].strip()
        GlassCoverage = policy[11].strip()
        LoanerCar = policy[12].strip()
        PaymentMethod = policy[13].strip()
        TotalPolicy = float(policy[14])

        if PaymentMethod == "Monthly":
        # Calculations
            ExtLiabilityCost = EXTRA_LIABILITY * NumCars if OptLiability == "Y" else 0
            GlassCoverageCost = GLASS_COVERAGE * NumCars if GlassCoverage == "Y" else 0
            LoanerCarCost = LOANER_CAR_OPTION * NumCars if LoanerCar == "Y" else 0

            ExtraCosts = ExtLiabilityCost + GlassCoverageCost + LoanerCarCost
            Subtotal = TotalPolicy + ExtraCosts
            HST = Subtotal * HST_RATE
            TotalCost = Subtotal + HST
            MonthlyPayment = (TotalCost + MONTHLY_PAYMENT)/12

            Subtotal += 1
            TotalSubtotal += Subtotal
            TotalHST += HST
            TotalPremium += TotalCost
            TotalMonthlyPayment += MonthlyPayment

            print("{:<5} {:<20}   {:>10} {:>10}  {:>10} {:>10}".format(PolNum, CustFirstName + " " + CustLastName, FV.FDollar2(TotalPolicy), FV.FDollar2(HST), FV.FDollar2(TotalCost), FV.FDollar2(MonthlyPayment)))

    print("=" * 73)
    print(f"Total policies:{TotalPolicies:>3d}", " " * 9,
          f"{FV.FDollar2(TotalSubtotal):>10s} {FV.FDollar2(TotalHST):>10s} "
          f" {FV.FDollar2(TotalPremium):>10s} {FV.FDollar2(TotalMonthlyPayment):>10s}")

