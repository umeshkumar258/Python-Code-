def get_number(prompt):
    """Safely get an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")


def generate_table(n, limit=10):
    """Generate multiplication table as a list."""
    return [f"{n} × {i} = {n * i}" for i in range(1, limit + 1)]


def display_table(table):
    """Display the multiplication table."""
    print("\n📊 Multiplication Table:\n")
    for line in table:
        print(line)


def main():
    print("=== Multiplication Table Generator ===")

    number = get_number("Enter a number: ")
    limit = get_number("Enter range (e.g., 10): ")

    table = generate_table(number, limit)
    display_table(table)


if __name__ == "__main__":
    main()
