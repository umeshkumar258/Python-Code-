def get_numbers(count=4):
    numbers = []

    for i in range(count):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("❌ Please enter a valid integer.")

    return numbers


def main():
    numbers = get_numbers()

    numbers.sort()

    print("\n📊 Sorted list:", numbers)
    print("🔝 Largest number:", numbers[-1])


if __name__ == "__main__":
    main()
