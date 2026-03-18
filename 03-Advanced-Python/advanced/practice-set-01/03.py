# ---------------------------------------
# MULTIPLICATION TABLE - IMPROVED
# ---------------------------------------

def generate_table(n, limit=10):
    return [n * i for i in range(1, limit + 1)]


def display_table(n, limit=10):
    print("\n📘 Formatted Table:")
    for i in range(1, limit + 1):
        print(f"{n} × {i} = {n * i}")


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------
try:
    n = int(input("Enter the number: "))
except ValueError:
    print("❌ Please enter a valid integer.")
else:
    table = generate_table(n)

    print("\n📋 Table (list comprehension):")
    print(table)

    display_table(n)

    print("\n📋 Table (using loop):")
    table_loop = []
    for i in range(1, 11):
        table_loop.append(n * i)
    print(table_loop)

print("\n✅ End of program")
