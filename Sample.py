import datetime


def read_defaults_file():
    with open("OSICDef.dat", "r") as file:
        policy_number = int(file.readline())
        basic_premium = float(file.readline())
        discount_additional_cars = float(file.readline())
        extra_liability_cost = float(file.readline())
        glass_coverage_cost = float(file.readline())
        loaner_car_cost = float(file.readline())
        hst_rate = float(file.readline())
        processing_fee = float(file.readline())

    return (policy_number, basic_premium, discount_additional_cars, extra_liability_cost,
            glass_coverage_cost, loaner_car_cost, hst_rate, processing_fee)


def write_defaults_file(policy_number, basic_premium, discount_additional_cars, extra_liability_cost,
                        glass_coverage_cost, loaner_car_cost, hst_rate, processing_fee):
    with open("OSICDef.dat", "w") as file:
        file.write(str(policy_number) + "\n")
        file.write(str(basic_premium) + "\n")
        file.write(str(discount_additional_cars) + "\n")
        file.write(str(extra_liability_cost) + "\n")
        file.write(str(glass_coverage_cost) + "\n")
        file.write(str(loaner_car_cost) + "\n")
        file.write(str(hst_rate) + "\n")
        file.write(str(processing_fee))


def calculate_total_insurance_premium(cars_count, basic_premium, discount_additional_cars,
                                      extra_liability_cost, glass_coverage_cost, loaner_car_cost):
    total_extra_costs = (cars_count - 1) * (basic_premium * discount_additional_cars)
    total_extra_costs += cars_count * extra_liability_cost
    total_extra_costs += cars_count * glass_coverage_cost
    total_extra_costs += cars_count * loaner_car_cost

    total_insurance_premium = basic_premium + total_extra_costs
    return total_insurance_premium


def main():
    policy_number, basic_premium, discount_additional_cars, extra_liability_cost, \
    glass_coverage_cost, loaner_car_cost, hst_rate, processing_fee = read_defaults_file()

    customer_policies = []

    while True:
        first_name = input("Enter customer's first name: ")
        last_name = input("Enter customer's last name: ")
        address = input("Enter customer's address: ")
        city = input("Enter customer's city: ").title()
        province_list = ["AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE", "QC", "SK", "YT"]
        province = input("Enter customer's province (2-letter code): ").upper()
        while province not in province_list:
            print("Invalid province code. Please enter a valid 2-letter code.")
            province = input("Enter customer's province (2-letter code): ").upper()

        postal_code = input("Enter customer's postal code: ")
        phone_number = input("Enter customer's phone number: ")
        cars_count = int(input("Enter the number of cars being insured: "))
        extra_liability = input("Extra liability coverage (Y or N): ").upper()
        glass_coverage = input("Glass coverage (Y or N): ").upper()
        loaner_car = input("Loaner car coverage (Y or N): ").upper()
        payment_method_list = ["FULL", "MONTHLY"]
        payment_method = input("Payment method (Full or Monthly): ").upper()
        while payment_method not in payment_method_list:
            print("Invalid payment method. Please enter 'Full' or 'Monthly'.")
            payment_method = input("Payment method (Full or Monthly): ").upper()

        total_insurance_premium = calculate_total_insurance_premium(cars_count, basic_premium,
                                                                    discount_additional_cars,
                                                                    extra_liability_cost,
                                                                    glass_coverage_cost,
                                                                    loaner_car_cost)

        hst_amount = total_insurance_premium * hst_rate
        total_cost = total_insurance_premium + hst_amount

        if payment_method == "MONTHLY":
            monthly_payment = (total_cost + processing_fee) / 8
        else:
            monthly_payment = None

        invoice_date = datetime.datetime.now().strftime("%Y-%m-%d")
        next_payment_date = (datetime.datetime.now() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")

        policy_info = f"{policy_number}, {invoice_date}, {first_name.title()}, {last_name.title()}, {address}, " \
                      f"{city}, {province}, {postal_code}, {phone_number}, {cars_count}, " \
                      f"{extra_liability}, {glass_coverage}, {loaner_car}, {payment_method}, " \
                      f"{total_insurance_premium:.2f}"

        customer_policies.append(policy_info)
        policy_number += 1

        print("\nPolicy information processed and saved.")

        another_policy = input("Do you want to enter another policy? (Y or N): ").upper()
        if another_policy != "Y":
            break

    write_defaults_file(policy_number, basic_premium, discount_additional_cars, extra_liability_cost,
                        glass_coverage_cost, loaner_car_cost, hst_rate, processing_fee)

    with open("Policies.dat", "a") as file:
        for policy_info in customer_policies:
            file.write(policy_info + "\n")


if __name__ == "__main__":
    main()