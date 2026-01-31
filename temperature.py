def convert_cel_to_far(C):
    F = C * (9/5) + 32
    return F

def convert_far_to_cel(F):
    C = (F - 32) * (5/9)
    return C

get_far = float(input("Enter Fahrenheit temperature: "))
the_cel = convert_far_to_cel(get_far)
print(f"{get_far} degrees Fahrenheit is {the_cel:.2f} degrees Celsius")
print()
print()
get_cel = float(input("Enter Celsius temperature: "))
the_far = convert_cel_to_far(get_cel)
print(f"{get_cel} degrees Celsius is {the_far:.2f} degrees Fahrenheit")

