# ---------------------------------------
# Function Definition
# ---------------------------------------
def good_day(name):
    """Greets the user"""
    print(f"Good morning, {name} 😊")


# ---------------------------------------
# Function Call using loop
# ---------------------------------------
for i in range(3):
    user_name = input("Enter your name: ")
    good_day(user_name)
