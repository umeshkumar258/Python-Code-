# ---------------------------------------
# Function to calculate average
# ---------------------------------------
def average_of_numbers(count=3):
    """Takes 'count' numbers from the user and returns their average"""
    
    numbers = []

    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    return sum(numbers) / count


# ---------------------------------------
# Function Call (Multiple Times)
# ---------------------------------------
for i in range(3):
    result = average_of_numbers()
    print(f"Average {i + 1}: {result}\n")

print("End of the program")


# ---------------------------------------
# Built-in sum() example with variables
# ---------------------------------------
def average_using_variables(a, b, c):
    """Returns the average of three numbers"""
    return (a + b + c) / 3


a = 39
b = 390
c = 300

avgn = average_using_variables(a, b, c)
print("\nAverage using variables:", avgn)
