def get_even_odd_list(n: int) -> list[tuple[int, str]]:
    """Generates even/odd classification for numbers 0 through n."""
    return [(i, "Even" if i % 2 == 0 else "Odd") for i in range(n + 1)]


def main() -> None:
    while True:
        try:
            user_input = input("Enter a positive number: ").strip()
            number = int(user_input)
            
            if number < 0:
                print("Please enter a non-negative number.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")

    print("\nEven / Odd Results:\n")
    results = get_even_odd_list(number)
    
    for num, status in results:
        print(f"{num:>3} -> {status}")


if __name__ == "__main__":
    main()
