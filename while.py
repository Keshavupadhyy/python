#while loop = perform some code WHILE some condition remains true

# example 1
# name = input("enter your name: ")
# while name == "":
#     print("you didi not enter your name")
#     name = input("enter your name: ")
#     print(f"Hello {name}")

# example 2

# age = int(input("enter your age: "))
# while age < 0:
#     print("Please enter the valid age")
#     age = int(input("enter your age: "))
#
# print(f"you are {age} years old")

# example 3

# food = input("Ente a food you like (q to like): ")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("Ente anthor a food you like (q to like): ")
#
# print("bye")

# # example 4

num = int(input("Enter a number 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number 1 - 10: "))

print(f"your number is valid {num}")


