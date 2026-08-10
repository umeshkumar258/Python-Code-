# Fruit List Program

def get_fruits(count):
    fruits = []

    for i in range(count):
        fruit = input("Enter fruit: ")

        while fruit == "":
            print("Please enter a fruit!")
            fruit = input("Enter fruit: ")

        fruits.append(fruit.capitalize())

    return fruits


def display_fruits(fruits):
    print("\nYour Fruit List:")

    for i, fruit in enumerate(fruits, start=1):
        print(i, fruit)


def fruit_list():
    print("Fruit List Program")
    print("------------------")

    count = int(input("How many fruits? "))

    fruits = get_fruits(count)

    display_fruits(fruits)


# Run the program
if __name__ == "__main__":
    fruit_list()
