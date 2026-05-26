# -------- SIMPLE SUM OF LIST ELEMENTS --------

numbers = []

count = int(input("How many numbers? "))

for i in range(count):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total = sum(numbers)

print("\n📘 List:", numbers)
print("➕ Sum:", total)
print("📊 Average:", total / count)
