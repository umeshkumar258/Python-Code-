def greatest(numbers):
    return max(numbers)


# Taking input from the user
nums = []
for i in range(3):
    num = float(input(f"Enter number {i + 1}: "))
    nums.append(num)

# Finding the greatest number
result = greatest(nums)

print(f"The greatest number is: {result}")
