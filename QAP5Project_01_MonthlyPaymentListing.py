import datetime

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

def calculate_monthly_payment(total_cost):
    processing_fee = 39.99
    total_cost += processing_fee
    return total_cost / 12

def generate_exception_report(policies):
    print("1234567890123456789012345678901234567890123456789012345678901234567890")
    print("ONE STOP INSURANCE COMPANY")
    print("MONTHLY PAYMENT LISTING AS OF", datetime.date.today().strftime('%d-%b-%y'))
    print("POLICY CUSTOMER TOTAL TOTAL MONTHLY")
    print("NUMBER NAME PREMIUM HST COST PAYMENT")
    print("=" * 69)

    total_policies = 0
    total_premium = 0
    total_extra_costs = 0

    for policy in policies:
        policy_number, _, first_name, last_name, _, _, _, _, _, _, _, _, payment_method, insurance_premium = policy
        if payment_method.strip().lower() == 'monthly':
            total_policies += 1
            extra_costs = calculate_extra_costs(policy)
            total_extra_costs += extra_costs
            total_premium += float(insurance_premium) + extra_costs
            hst = total_premium * 0.15
            total_cost = total_premium + hst
            monthly_payment = calculate_monthly_payment(total_cost)

            print(f"{policy_number} {first_name} {last_name} ${insurance_premium} ${hst:.2f} ${total_cost:.2f} ${monthly_payment:.2f}")

    print("=" * 69)
    print(f"Total policies: {total_policies} ${total_premium:.2f} ${total_extra_costs:.2f} ${total_premium + total_extra_costs:.2f}")

if __name__ == "__main__":
    policies_data = read_data_file('Policies.dat')
    generate_exception_report(policies_data)
