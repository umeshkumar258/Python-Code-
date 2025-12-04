first = int(input("Enter the numeber: "))

if(first % 400 == 0 or (first % 100 != 0 and first % 4 == 0 )):
    print("it is leap year")

else:
    print("it is not ")