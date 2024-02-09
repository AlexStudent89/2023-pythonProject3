# The One Stop Company Policy Listing
# Written by Alex Ewida
# Written on August 1, 2023
import csv
import datetime

#Constants
EXTRA_LIABILITY = 130
GLASS_COVERAGE = 86
LOANER_CAR_OPTION = 58

def calculate_extra_costs(record):
    extra_liability_cost = 130.00 if record[8].upper() == 'Y' else 0.00
    glass_coverage_cost = 86.00 if record[9].upper() == 'Y' else 0.00
    loaner_car_cost = 58.00 if record[10].upper() == 'Y' else 0.00
    total_extra_costs = extra_liability_cost + glass_coverage_cost + loaner_car_cost
    return total_extra_costs

def generate_detailed_report(records):
    total_policies = len(records)
    total_insurance_premium = sum(float(record[-1]) for record in records)
    total_extra_costs = sum(calculate_extra_costs(record) for record in records)
    total_premium = total_insurance_premium + total_extra_costs

    print("ONE STOP INSURANCE COMPANY")
    print("POLICY LISTING AS OF dd-Mon-yy")
    print()
    print("POLICY CUSTOMER                  POLICY      INSURANCE     EXTRA    TOTAL")
    print("NUMBER NAME                       DATE        PREMIUM      COSTS   PREMIUM")
    print("=" * 74)

    for record in records:
        print(f"{record[0]:<4} {record[2]:<25} {record[1]:<10} ${record[-1]:>9} ${calculate_extra_costs(record):>9} ${float(record[-1]) + calculate_extra_costs(record):>9.2f}")

    print("=" * 74)
    print(f"Total policies: {total_policies}                        ${total_insurance_premium:>9.2f} ${total_extra_costs:>9.2f} ${total_premium:>9.2f}")

if __name__ == "__main__":
    with open("PoliciesData.dat", "r") as file:
        data_lines = file.readlines()

    records = [line.strip().split(", ") for line in data_lines]

    with open("detailed_report.txt", "w") as output_file:
        generate_detailed_report(records)

