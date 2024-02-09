# Program to determine the existing club members, and add new members as they are accepted.
# Author: Alex Ewida
# Date written: May 31, 2023
#  Member Receipt Summary
# Client name: Katharine Brown
CliName = input("Enter the Client's Name: ")
# Phone Number:
HomPhoneNum = input("Enter Home Phone Number:")
CliPhoneNum = input("Enter Client Phone Number:")
# The Marina has 100 sites.

# Site Number:
SitNum = int(input("Enter the Site Number (1-100):"))
# Member Info:
Issued = input("Date: (YYYY-MM-DD):")
MemName = input("Enter the Member Name:")
StrAdd = input("Enter the street address:")
City = input("Enter the city:")
Prov = input("Enter the province:")
PosCo = input("Enter the postal code:")
PhoneNum = input("Enter the phone number:")
CellNum = input("Enter the cell number:")
MemTyp= input("Enter the membership type (S or E):")

NumAltMem = int(input("Enter number of alternate members who will be allowed access to the grounds"))
# Weekly Site Cleaning
WeSiteCle = input("Weekly Site Cleaning (Y or N)")

# Video surveillance
VidSur = input("Video surveillance (Y or N)")

# Site charges: $
NumEveSitPerMon = 80.00
OdNumSit = 120.00
# Each alternate member costs per month: $
AltMem = 5.00

# Weekly site cleaning charge for chosen Member:
WeSitCleChar = 0
VidSurChar = 0
if WeSiteCle == "Y":
    WeSitCleChar = 50.00
if VidSur == "Y":
    VidSurChar = 35.00
ExChar = WeSitCleChar + VidSurChar

if (SitNum % 2) == 0:
    SitChar = NumEveSitPerMon
else:
    SitChar = OdNumSit

SitChar = NumAltMem * AltMem

SubTot = SitChar+ExChar
HST = 0.15*SubTot
TotMonChar = SitChar+ExChar+HST
MonDue = 0
if MemTyp == "S":
    MonDue = 75.00
elif MemTyp == "E":
    MonDue = 150.00
TotMonFee = TotMonChar + MonDue

ProcFee = 59.99
TotYeaFee = TotMonFee*12
MonPay = (TotYeaFee + ProcFee) / 12
CancelFee = 0.60 * TotYeaFee


print("St. John’s Marina & Yacht Club")
print(f"Client Name and Address: {CliName}")
print(f"Phone: {PhoneNum}")
print(f"Site: {SitNum}")
print(f"Member type: {MemTyp}")
print(f"Alternate members: {AltMem}")
print(f"Weekly site cleaning: {WeSiteCle}")
print(f"Video surveillance: {VidSur}")
print(f"Site charges: {SitChar}")
print(f"Extra charges: {ExChar}")
print(f"Subtotal: {SubTot}")
print(f"Sales tax (HST): {HST}")
print(f"Total monthly charges: {TotMonChar}")
print(f"Monthly dues: {MonDue}")
print(f"Total monthly fees: {TotMonFee}")
print(f"Total yearly fees: {TotYeaFee}")
print(f"Monthly payment: {MonPay}")
print(f"Issued: YYYY-MM-DD")
print(f"HST Reg No: 549-33-5849-4720-9885")
print(f"Cancellation fee: {CancelFee}")

