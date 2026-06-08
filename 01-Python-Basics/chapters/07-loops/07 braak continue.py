# Break Example
print("--- Break Example ---")

for i in range(10):
    if i == 2:
        print("Break triggered")
        break
    print(i)


# Continue Example
print("\n--- Continue Example ---")

for i in range(10):
    if i == 4:
        continue
    print(i)
