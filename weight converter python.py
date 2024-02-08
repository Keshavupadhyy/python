weight = float(input("enter your weight"))
unit = input("killograms or pound? (K or L):")
if unit == "K":
    weight = weight * 2.205
    unit = "kilogram."
    print(f"Your weight is:{weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "pound."
    print(f"Your weight is:{weight} {unit}")
else:
    print("Please valid unit???")

