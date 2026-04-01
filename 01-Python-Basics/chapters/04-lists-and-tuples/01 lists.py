def main():
    # A list can store different data types
    items = ["Umesh", "orange", 6, 83, "Harry", 999]

    print("📌 Original List:", items)
    print("📌 Type of variable:", type(items))

    # Indexing
    print("\n🔹 Indexing")
    print("First element:", items[0])
    print("Last element:", items[-1])

    # Lists are mutable
    print("\n🔹 Updating Elements")
    items[0] = "Appu"
    print("After updating first element:", items)

    # List slicing
    print("\n🔹 Slicing")
    print("From index 0 to end:", items[0:])
    print("Full list copy:", items[:])
    print("Slice [1:3]:", items[1:3])

    # Append new value
    print("\n🔹 Append Operation")
    items.append("UmeshKumar")
    print("After append:", items)

    # Modify another element
    items[3] = "Umesh"
    print("After modifying index 3:", items)

    # Another list example
    print("\n🔹 Another List Example")
    friends = ["John", "Doe", "Alice", "Bob"]
    print("Friends list:", friends)
    print("Friends slice [1:3]:", friends[1:3])

    print("\n✅ Final Output")
    print("Items list:", items)
    print("Friends list:", friends)


# Run the program
if __name__ == "__main__":
    main()
