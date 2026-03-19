

n = int(input("Enter the number the values is there: "))

# Generate table using list comprehension
table = [n * i for i in range(1, 11)]

with open("table.txt", "a") as f:
    f.write(f"\nMultiplication Table of {n}\n")
    for i, value in enumerate(table, start=1):
        f.write(f"{n} x {i} = {value}\n")

print("✅ Table written to file successfully.")
print("it was good")
