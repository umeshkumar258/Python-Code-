# -------- IMPROVED SUM OF LIST ELEMENTS --------

def get_numbers():
    numbers = []
    
    try:
        count = int(input("How many numbers do you want to enter? "))
        if count <= 0:
            print("❌ Enter a number greater than 0.")
            return []
    except ValueError:
        print("❌ Invalid input.")
        return []

    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("⚠️ Please enter a valid number.")
    
    return numbers


def display_result(numbers):
    if not numbers:
        print("⚠️ No data to calculate.")
        return

    total = sum(numbers)

    print("\n📘 List:", numbers)
    print("➕ Sum of elements:", total)
    print("🔢 Total elements:", len(numbers))
    print("📊 Average value:", total / len(numbers))


def sum_of_list():
    print("📘 Sum of List Program")
    print("-" * 30)

    numbers = get_numbers()
    display_result(numbers)


# Run program
if __name__ == "__main__":
    sum_of_list()
