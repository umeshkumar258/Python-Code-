def get_numbers(count=3):
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


def calculate_result(numbers):
    average = sum(numbers) / len(numbers)

    if average > 40:
        result = "He scores good"
    elif average >= 33:
        result = "He is pass"
    else:
        result = "Fail"

    return average, result


def main():
    numbers = get_numbers()
    average, result = calculate_result(numbers)

    print("\n📊 Numbers:", numbers)
    print("📈 Average =", average)
    print("📢 Result:", result)


if __name__ == "__main__":
    main()
