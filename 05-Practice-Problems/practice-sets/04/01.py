# -------- FRUIT LIST PROGRAM --------

def fruit_list():
    fruits = []

    print("🍎 Fruit List Program")
    print("-" * 25)

    for i in range(5):
        fruit = input(f"Enter fruit {i+1}: ")
        fruits.append(fruit)

    print("\n📋 Fruits List:")
    print(fruits)

# Function call
fruit_list()
