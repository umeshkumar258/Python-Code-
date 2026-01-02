# List of numbers
nums = [384, 48, 593, 3]

print("Using normal for loop:")
index = -1
for item in nums:
    index += 1
    print(f"The item number at index {index} is {item}")

print("\nUsing enumerate function:")
for index, item in enumerate(nums):
    print(f"The item number at index {index} is {item}")
