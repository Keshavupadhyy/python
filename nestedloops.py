# nested loop = A loop within another loop (outer, inner)
# outer loop:
# inner loop:

#
# for x in range(3):
#     print()
#     for x in range(1, 10):
#         print(x, end="")

# print rectangle

rows = int(input("Enter the number of rows: "))
columns = int(input("enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for x in range(columns):
        print(symbol, end=" ")
    print()