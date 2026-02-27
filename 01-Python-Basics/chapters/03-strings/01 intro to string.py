# String creation
first_name = "Umesh"
duplicate_name = first_name  # No need for slicing copy

# String slicing
short_name = first_name[:3]
print(f"Short name: {short_name}")

# Full string
print(f"Full name: {first_name}")

# Type checking
print(f"Type of first_name: {type(first_name)}")

# Demonstrating immutability
modified_name = "U" + first_name[1:]
print(f"Modified name: {modified_name}")

# String concatenation
combined_name = first_name + duplicate_name
print(f"Concatenated name: {combined_name}")
