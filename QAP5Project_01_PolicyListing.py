# Compare this snippet from

import datetime
import re

    def read_data_file(file_name):
        policies = []
        with open(file_name, 'r') as file:
            for line in file:
                policy_data = line.strip().split(',')
                policies.append(policy_data)
        return policies

    def calculate_extra_costs(data):
        extra_liability_cost = 130.00 if data[9] == 'Y' else 0
        glass_coverage_cost = 86.00 if data[10] == 'Y' else 0
        loaner_car_cost = 58.00 if data[11] == 'Y' else 0
        return extra_liability_cost + glass_coverage_cost + loaner_car_cost

    def generate_detailed_report(policies):
        print("1234567890123456789012345678901234567890123456789012345678901234567890")
        print("ONE STOP INSURANCE COMPANY")
        print("POLICY LISTING AS OF", datetime.date.today().strftime('%d-%b-%y'))
        print("POLICY CUSTOMER POLICY INSURANCE EXTRA TOTAL")
        print("NUMBER NAME DATE PREMIUM COSTS PREMIUM")
        print("=" * 73)

        total_policies = 0
        total_premium = 0
        total_extra_costs = 0

        for policy in policies:
            policy_number, invoice_date, first_name, last_name, _, _, _, _, _, _, _, _, payment_method, insurance_premium = policy
            total_policies += 1
            extra_costs = calculate_extra_costs(policy)
            total_extra_costs += extra_costs
            total_premium += float(insurance_premium) + extra_costs

            print(f"{policy_number} {first_name} {last_name} {invoice_date} ${insurance_premium} ${extra_costs:.2f} ${float(insurance_premium) + extra_costs:.2f}")

        print("=" * 73)
        print(f"Total policies: {total_policies} ${total_premium:.2f}")

    if __name__ == "__main__":
        policies_data = read_data_file('Delete.dat')
        generate_detailed_report(policies_data)
