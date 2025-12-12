# -------------------------
# Example 1: Break Statement
# -------------------------

print("Using break:")
for i in range(101):
    if i == 2:
        print("Break triggered at i =", i)
        break     # Exits the loop immediately
    print(i)


# -------------------------
# Example 2: Continue Statement
# -------------------------

print("\nUsing continue:")
for i in range(10):
    if i == 4:
        print("Skipping i =", i)
        continue   # Skips this iteration only
    print(i)
