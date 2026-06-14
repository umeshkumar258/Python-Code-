# Count the number of zeros in a tuple

numbers = (7, 0, 8, 0, 0, 9)

print("Tuple:", numbers)

count = numbers.count(0)

print("Number of zeros:", count)

if count > 0:
    print("Zeros are present in the tuple")
else:
    print("No zeros found in the tuple")
