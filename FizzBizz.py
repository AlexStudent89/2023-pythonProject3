def calculate_FizzBizz():
    print()
    for n in range(100):
        if n % 5 == 0 and n % 8 == 0:
            print("FizzBizz")
        elif n % 5 == 0:
            print("Fizz")
        elif n % 8 == 0:
            print("Bizz")
        else:
            print(n)
    cont = input("Press any key to continue...")
    print("Returning to Main Menu")
    print()