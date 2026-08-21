# Take 3 numbers as input
numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(3)]

# Find and print the greatest number
print("The greatest number is:", max(numbers))
