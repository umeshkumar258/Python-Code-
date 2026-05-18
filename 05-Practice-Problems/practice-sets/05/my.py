# -------------------------------
# Simple Set Program
# -------------------------------

# Creating an empty set
numbers = set()

# Taking 5 inputs from user
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.add(num)

# Displaying set
print("\nSet:", numbers)

# Adding element
numbers.add(100)
print("\nAfter adding 100:", numbers)

# Removing element
numbers.remove(100)
print("After removing 100:", numbers)

# Checking element
print("\nIs 10 present?", 10 in numbers)

# Length of set
print("Total elements:", len(numbers))

# Important Notes
print("\nImportant Notes:")
print("- Sets do not allow duplicate values")
print("- Sets are unordered")
print("- Sets store immutable values only")
print("- Empty set is created using set()")
