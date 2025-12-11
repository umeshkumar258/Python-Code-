# Print numbers from 1 to 50 using a while loop
i = 1  # Starting point

while i < 51:
    print(i)
    i += 1   # Increase i by 1 (very important to avoid an infinite loop)


# Print even numbers using a while loop
j = 2  # Start from 2

# This condition means: run only when both conditions are true
while j < 15 and j < 10:
    print(j)
    j += 2   # Increase by 2 each time


# Note:
# Logical operators (and, or, not) can be used inside loops and conditions.
