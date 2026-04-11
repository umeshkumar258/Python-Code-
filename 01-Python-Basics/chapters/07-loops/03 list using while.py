items = [4, "umesh", 38, 383, "harry"]

# Start=1 makes the human-readable count begin at 1 instead of 0
for index, item in enumerate(items, start=1):
    print(f"Position {index}: {item}")
