# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 322021.1589
price2 = -98456449.65
price3 = 125645185.34

print(f"price1 is {price1:%}")
print(f"price2 is {price2:%}")
print(f"price3 is {price3:%}")

