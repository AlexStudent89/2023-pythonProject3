# Adding a new conference center to the hotel:

import csv

# Function to read default values from Defaults.dat
def main():
 def print_string(s):
    print(s.abc())
    while True:
        try:
            with open("Defaults.dat", "r") as file:
                Next_Conference_Number = int(file.readline())
                HST_Rate = float(file.readline())
                Small_Conference_Room_Cost = float(file.readline())
                Medium_Conference_Room_Cost = float(file.readline())
                Large_Conference_Room_Cost = float(file.readline())
                Cost_per_Person_for_Breakfast = float(file.readline())
                Cost_per_Person_for_Lunch = float(file.readline())
                Cost_per_Person_for_Supper = float(file.readline())
                Cost_per_Person_for_Coffee_Break = float(file.readline())
        except:
            print("Defaults.dat does not exist.")
            exit()
        else:
            print()
            print("Defaults.dat exists.")
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
            conference_title = input("Enter conference title: ")
            if conference_title == "":
                print("Invalid conference title. Please enter a valid conference title.")
            else:
                break
        while True:
            StartDateConfer = input("Enter start date of the conference (YYYY-MM-DD): ")
            start_date = datetime.strptime(StartDateConfer, '%Y-%m-%d')
            if StartDateConfer == "":
                print("Invalid start date of conference. Please enter a valid start date.")
            else:
                break
        while True:
            try:
                total_days = int(input("Enter the number of days for the conference: "))
                if total_days > 0:
                    return total_days
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid number of days.")


