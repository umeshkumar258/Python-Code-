# ---------------------------------------
# 1. Function with user input
# ---------------------------------------
def good_day():
    """Greets the user with their name"""
    user = input("Enter your name: ")
    print(f"Good day, {user} 😊")

good_day()


# ---------------------------------------
# 2. Simple function (no parameters)
# ---------------------------------------
def show_message():
    print("This is a function")

show_message()


# ---------------------------------------
# 3. Function with parameters
# ---------------------------------------
def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("Umesh")


# ---------------------------------------
# 4. Function with return value
# ---------------------------------------
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# ---------------------------------------
# 5. Default parameter
# ---------------------------------------
def country_name(country="India"):
    print(f"I am from {country}")

country_name()
country_name("USA")


# ---------------------------------------
# 6. Function called inside a loop
# ---------------------------------------
def square(num):
    return num * num

print("\nSquares from 1 to 5:")
for i in range(1, 6):
    print(square(i))


# ---------------------------------------
# 7. Lambda function (short form)
# ---------------------------------------
multiply = lambda x, y: x * y
print("\nMultiplication:", multiply(4, 5))
