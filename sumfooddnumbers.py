# if the given range is 10
given_range = 10

# set up a variable to store the sum
# with initial value of 0
sum = 0

for i in range(given_range):

    # if i is odd, add it
    # to the sum variable
    if i % 2 != 0:
        sum += i

# print the total sum at the end
print(sum)