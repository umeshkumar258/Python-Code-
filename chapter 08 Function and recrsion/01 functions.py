
#   Function Definition

def avg():
    numbers = [int(input("Enter the number:")) for _ in range(3)]
    print(sum(numbers) / 3)

   # Function Call
for i in range(3):
    avg()

print("End of the program")
#sum() # This is built in function return sum of listed numbers


a = 39
b =390
c = 300

avgn = (a + b + c) / 3
print(avgn)