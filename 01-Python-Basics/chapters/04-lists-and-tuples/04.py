def count_zeros(data):
    return data.count(0)


def main():
    numbers = (7, 0, 8, 0, 0, 9)
    zero_count = count_zeros(numbers)

    print(f"Tuple: {numbers}")
    print(f"Number of zeros: {zero_count}")


if __name__ == "__main__":
    main()
