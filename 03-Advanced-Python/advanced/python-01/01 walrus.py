# Python Walrus Operator (:=) - Improved Version
# Requires Python 3.8+

from functools import reduce

# -------------------------------
# 1. Length checking
# -------------------------------
numbers = [1, 2, 3, 4, 5]

if (n := len(numbers)) > 3:
    print(f"⚠️ List is too long ({n} elements), expected ≤ 3")
else:
    print(f"✅ List length is acceptable ({n} elements)")


# -------------------------------
# 2. Input validation
# -------------------------------
name = input("\nEnter your name: ").strip()

if name:
    print(f"👋 Hello, {name}")
else:
    print("❌ Name cannot be empty")


# -------------------------------
# 3. While loop with safe input
# -------------------------------
print("\nEnter numbers (0 to stop):")

while True:
    try:
        if (num := int(input("Enter number: "))) == 0:
            print("🛑 Stopped by user")
            break
        print(f"➡️ You entered: {num}")
    except ValueError:
        print("❌ Please enter a valid integer!")


# -------------------------------
# 4. Data check example
# -------------------------------
data = "Hello Python"

if (content := data):
    print(f"\n📄 Data found: {content}")
else:
    print("❌ No data found")


# -------------------------------
# 5. Maximum value (cleaner way)
# -------------------------------
values = [10, 45, 23, 99, 67]

# Using walrus operator
if values and (maximum := max(values)):
    print(f"\n🏆 Maximum value: {maximum}")
else:
    print("❌ Empty list")


# -------------------------------
# 6. Comparison without walrus
# -------------------------------
length = len(values)

if length > 3:
    print(f"📊 Values list has {length} elements")
else:
    print("📊 List has 3 or fewer elements")

print("\n✅ Program completed successfully")
