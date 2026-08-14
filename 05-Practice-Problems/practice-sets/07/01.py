def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def multiplication_table(number, limit):
    table = []

    for i in range(1, limit + 1):
        table.append(f"{number} × {i} = {number * i}")

    return table


def main():
    print("=== Multiplication Table Generator ===")

    number = get_number("Enter a number: ")
    limit = get_number("Enter the range: ")

    table = multiplication_table(number, limit)

    print("\nMultiplication Table:")
    for line in table:
        print(line)


main()
