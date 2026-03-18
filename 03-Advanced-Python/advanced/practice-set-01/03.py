




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
