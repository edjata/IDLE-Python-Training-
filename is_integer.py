num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

print(f"The difference between {num1} and {num2} is an integer?", (num1 - num2).is_integer())
