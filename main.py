# Author: Alex Ewida, Mohamed Maghrebi, Manny Nwokedi
# Written: June 20, 2023
# Program for the NL Chocolate Company

import FormatValues as FV
import travel_claim as TC
import FizzBizz as FB

def main():
    # Main Menu
    print()
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()


    while True:
        print()
        print("1. Enter an Employee Travel Claim.")
        print("2. Fun Interview Question.")
        print("3. Cool Stuff with Strings and Dates.")
        print("4. Something Old, Something New")
        print("5. Quit Program.")
        print()
        try:
            choice = int(input("   Enter choice (1-5): "))
        except:
            print("Error - choice is not a valid entry.")
        else:
            if not 1 <= choice <= 5:
                print("Error - Choice must be between 1 and 5.")
            elif choice == 1:
                TC.calculate_travel_claim()
            elif choice == 2:
                FB.calculate_FizzBizz()
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            else:
                print("Thanks, goodbye.")
                exit()

main()