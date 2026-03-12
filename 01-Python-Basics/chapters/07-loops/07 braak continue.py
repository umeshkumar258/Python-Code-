# ---------------------------------------
# Example 1: Break Statement
# ---------------------------------------

def break_example():
    print("\n--- Break Example ---")

    for i in range(101):
        if i == 2:
            print(f"Break triggered at i = {i}")
            break
        print(i)


# ---------------------------------------
# Example 2: Continue Statement
# ---------------------------------------

def continue_example():
    print("\n--- Continue Example ---")

    for i in range(10):
        if i == 4:
            print(f"Skipping i = {i}")
            continue
        print(i)


# ---------------------------------------
# Run Examples
# ---------------------------------------

break_example()
continue_example()
