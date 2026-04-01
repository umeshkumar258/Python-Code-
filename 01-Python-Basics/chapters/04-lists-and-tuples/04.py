def count_zeros(data):
    """Return the number of zeros in the given iterable."""
    return data.count(0)


def main():
    numbers = (7, 0, 8, 0, 0, 9)

    print("🔹 Tuple:", numbers)

    zero_count = count_zeros(numbers)
    print("🔹 Number of zeros:", zero_count)

    # Extra: Check if no zeros
    if zero_count == 0:
        print("No zeros found in the tuple")
    else:
        print("Zeros are present in the tuple")


if __name__ == "__main__":
    main()
