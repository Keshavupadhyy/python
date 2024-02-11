# validate user input exercise
usename = input("Enter your username")
if len(usename) > 12:
    print(f"user name {usename}is not valid")
elif not usename.find(" ") == -1:
    print("invalid username detect spaces")
elif not  usename.isalpha():
    print("invalid username detect numbers")
else:
    print(f"welcome{usename}")