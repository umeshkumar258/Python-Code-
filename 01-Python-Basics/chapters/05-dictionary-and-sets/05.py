# Create an empty set
numbers = set()

# Add elements
numbers.add(20)
numbers.add(20.0)  # Same value as 20, won't be added
numbers.add("20")  # String, so it will be added

# Display the set
print(numbers)
print("Length:", len(numbers))
