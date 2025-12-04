n = int(input("enter the number:"))

i = 0
sum = 0
while(i<=n):
    sum += i
    i += 1


print(sum)

n = int(input("Enter the number:"))

sum = 0
for i in range(n+1):  # This will loop from i = 0 to i = n (inclusive)
    sum += i  # Add the current value of i to sum

print(sum)
