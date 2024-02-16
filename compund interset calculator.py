principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount of: "))
    if principle <= 0:
        print("Priciple cant not b less than or equal to zero")

while rate <= 0:
   rate = float(input("Enter the  Interset rate amount of: "))
   if rate > 0:
       continue
   print("rate cant not b less than or equal to zero")

while time <= 0:
   time = float(input("Enter the time  of years: "))
   if time > 0:
       continue
   print("time cant not b less than or equal to zero")


total = principle * pow((1+rate/100),time)
print(f"balce after 1 year {total}")


#you use true and break keyword also