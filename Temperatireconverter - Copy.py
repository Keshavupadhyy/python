unit = input("Its is a temperatire in celsius or faherhenit (C/F):")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"the temperature in F is {temp}F")
elif unit == "f":
    temp = ((temp - 32) * 5 / 9)
    print(f"The temperature in celius is :{temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")
