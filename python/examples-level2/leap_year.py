year = int(input("Enter the year:"))

leap = False
if year%100 != 0 or year%400 ==0:
    leap =True
elif year%4 == 0:
    leap = True
else:
    leap= False
print(leap)