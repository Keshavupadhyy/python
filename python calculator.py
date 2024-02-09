operator = input("Enter an operator (+ - * /):")
num1 = float(input("enter a number1"))
num2 = float(input("enter a number2"))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"please enster valid {operator}")