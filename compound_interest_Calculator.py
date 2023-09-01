# Name: Thomas Alsop
# A Compound Interest Calulator


def print_intro():
    print("Welcome to the Wolving compound interest calculator. This ")
    print("program calculates your potential returns when you invest with us.")
    print("")


def get_input():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate amount: ")) / 100
    years = int(input("Enter the amount of years: "))
    return principal, rate, years


def simple_interest(principal, rate, years):
    return principal * (1 + rate * years)


def compound_interest(principal, rate, years):
    return principal * (1 + rate / 4) ** (4 * years)


def print_simple_output(principal, rate, years, simple_result):
    print('£{0:.2f} invested at {1:.1f}% for {2:} years is: £{3:,.2f}'.format(principal, rate * 100, years, simple_result))


def print_compounding_output(principal, rate, years, compound_result):
    print('£{0:.2f} invested at {1:.1f}% for {2:} years compounded 4 times a year is: £{3:,.2f}'.format(principal, rate * 100, years, compound_result))


def get_target_input():
    pass


def calculate_years_to_target():
    pass


def print_target_output():
    pass


def main():
    print_intro()
    principal, rate, years = get_input()
    simple_result = simple_interest(principal, rate, years)
    compound_result = compound_interest(principal, rate, years)
    print_simple_output(principal, rate, years, simple_result)
    print_compounding_output(principal, rate, years, compound_result)


if __name__ == '__main__':
    main()
