# -------- IMPROVED FRUIT LIST PROGRAM --------

def get_fruits(count):
    fruits = []
    for i in range(count):
        while True:
            fruit = input(f"Enter fruit {i + 1}: ").strip()
            if fruit:  # Avoid empty input
                fruits.append(fruit.capitalize())
                break
            else:
                print("⚠️ Please enter a valid fruit name.")
    return fruits


def display_fruits(fruits):
    print("\n📋 Your Fruit List:")
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}. {fruit}")


def fruit_list():
    print("🍎 Fruit List Program")
    print("-" * 30)

    try:
        count = int(input("How many fruits do you want to enter? "))
        if count <= 0:
            print("❌ Please enter a number greater than 0.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    fruits = get_fruits(count)
    display_fruits(fruits)


# Run the program
if __name__ == "__main__":
    fruit_list()
