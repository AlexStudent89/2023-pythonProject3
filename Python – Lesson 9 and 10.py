# Lesson 9 and 10
Age = input("Enter a persons age: ")
Age = int(Age)
if Age >= 19:  # comparison operators can be >, <, >=, <=, !=, ==
    # Block of text executed if the criteria is True.
    print("Allowed to vote.")
else:
    # Block of text executed if the criteria is False.
    print("Too young to vote.")

HourlyPayRate = input("Enter the hourly pay rate: ")
HourlyPayRate = float(HourlyPayRate)
HoursWorked = input("Enter the number of hours worked: ")
HoursWorked = int(HoursWorked)
if HoursWorked <= 40:
    GrossPay = HoursWorked * HourlyPayRate
else:
    RegPay = 40 * HourlyPayRate
    OTPay = (HourlyPayRate * 1.5) * (HoursWorked - 40)
    GrossPay = RegPay + OTPay
print(f"The gross pay is ${GrossPay}")

MarStat = input("Enter the marital status (S, M, W or O): ").upper()
if MarStat == "S":
    print("Single")
elif MarStat == "M":
    print("Married")
elif MarStat == "W":
    print("Widowed")
else:
    print("Other")

BalDue = input("Enter the customer balance due: ")
BalDue = float(BalDue)
CredLim = input("Enter the customer credit limit: ")
CredLim = float(CredLim)

if BalDue <= CredLim:
    PayDue = BalDue * .10
else:
    PayDue = (BalDue * .10) + (BalDue - CredLim)
print(f"Payment due:  ${PayDue}")

First = input("Enter the first integer value: ")
First = int(First)
Second = input("Enter the second integer value: ")
Second = int(Second)
Sum = First + Second
Diff = First - Second
Prod = First * Second
if Second != 0:
    Quot = First / Second
else:
    Message = "Division by 0."
if First % 2 == 0:
    FirstEO = "Even"
else:
    FirstEO = "Odd"
if Second % 2 == 0:
    SecondEO = "Even"
else:
    SecondEO = "Odd"
print(FirstEO)
print(SecondEO)
print(Sum)
print(Diff)
print(Prod)
if Second != 0:
    print(Quot)
else:
    print(Message)
