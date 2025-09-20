list = [384,48,593,3]

index = -1
for item in list:
    index +=1
    print(f"The item number {index} is {item}")


# this can be simplifed using enumerate funtion

for index , item in enumerate(list):
    print(f"The item numeber at index {index} is {item}")