# This program tracks the growing amount of an investment over time

# initial deposit principal
amount = float(input("Enter initial deposit amount: $"))

# fixed percentage annually
rate = float(input("Enter annual fixed rate: "))

# number of years
years = int(input("Enter number of years: "))

def invest(amount, rate, years):
    for n in range(years):
        amount = (amount * rate) + amount
        year = n + 1
        print(f"year {year}: ${amount:.2f}")

print()   
invest(amount, rate, years)
