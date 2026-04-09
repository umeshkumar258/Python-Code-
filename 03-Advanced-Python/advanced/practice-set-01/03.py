# ---------------------------------------
# FUNCTIONS
# ---------------------------------------

def generate_table(n):
    """Generate multiplication table using list comprehension"""
    return [n * i for i in range(1, 11)]


def display_table(n):
    """Display multiplication table in readable format"""
    print("\n📋 Table (formatted):")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------

try:
    n = int(input("Enter the number: "))
except ValueError:
    print("❌ Please enter a valid integer.")
else:
    # Using function (list comprehension)
    table = generate_table(n)
    print("\n📋 Table (list comprehension):")
    print(table)

    # Display formatted table
    display_table(n)

    # Using loop
    print("\n📋 Table (using loop):")
    table_loop = []
    for i in range(1, 11):
        table_loop.append(n * i)
    print(table_loop)

finally:
    print("\n✅ End of program")
