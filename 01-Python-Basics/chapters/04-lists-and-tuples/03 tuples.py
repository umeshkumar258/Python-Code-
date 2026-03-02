def main():
    # Tuple declaration
    numbers = (4, 484, 2, 384, 2)

    print(f"Type of numbers: {type(numbers)}")
    print(f"Value: {numbers}")
    print(f"Length: {len(numbers)}")

    # Count occurrences
    value_to_count = 2
    print(f"Count of {value_to_count}: {numbers.count(value_to_count)}")

    # Tuple repetition
    repeated_tuple = numbers * 3
    print(f"Tuple repeated 3 times: {repeated_tuple}")

    # Find first index safely
    try:
        index_value = numbers.index(value_to_count)
        print(f"First index of {value_to_count}: {index_value}")
    except ValueError:
        print(f"{value_to_count} not found in tuple")


if __name__ == "__main__":
    main()
