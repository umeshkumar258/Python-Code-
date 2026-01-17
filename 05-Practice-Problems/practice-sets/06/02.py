# Taking 3 numbers using list comprehension
a, b, c = [int(input("Enter your number: ")) for _ in range(3)]

# Calculating average
average = (a + b + c) / 3

# Result
if average > 40:
    print("He scores good")
elif average >= 33:
    print("He is pass")
else:
    print("Fail")

print("Average =", average)
