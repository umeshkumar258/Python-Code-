def show(step, value):
    print(f"{step:<35} -> {value}")


def main():
    # Tuple declaration
    numbers = (4, 484, 2, 384, 2)

    show("Type of numbers", type(numbers))
    show("Tuple values", numbers)
    show("Length", len(numbers))

    # Accessing elements
    print("\n🔹 Accessing Elements")
    show("First element", numbers[0])
    show("Last element", numbers[-1])
    show("Slice [1:4]", numbers[1:4])

    # Count occurrences
    print("\n🔹 Count & Index")
    value = 2
    show(f"Count of {value}", numbers.count(value))

    try:
        idx = numbers.index(value)
        show(f"First index of {value}", idx)
    except ValueError:
        print(f"{value} not found")

    # Tuple repetition
    print("\n🔹 Tuple Operations")
    repeated = numbers * 3
    show("Repeated 3 times", repeated)

    # Tuple concatenation
    new_tuple = numbers + (100, 200)
    show("After concatenation", new_tuple)

    # Immutability demonstration
    print("\n🔹 Immutability Check")
    try:
        numbers[0] = 10
    except TypeError:
        print("Tuples are immutable (cannot modify elements)")

    # Packing & Unpacking
    print("\n🔹 Packing & Unpacking")
    a, b, c, d, e = numbers
    show("Unpacked values", (a, b, c, d, e))

    show("Final tuple", numbers)


if __name__ == "__main__":
    main()
