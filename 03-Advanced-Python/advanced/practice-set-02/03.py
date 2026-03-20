

n = int(input("Enter the number : "))

table = [str(n * i) for i in range(1, 11)]

result = "\n".join(table)

print(f"Table of {n}:\n")
print(result)
