words = {"umesh", "appu", "harry", "babu"}

name = input("Enter the name: ").lower()

# Convert set items to lowercase for proper comparison
words = {w.lower() for w in words}

print("Good person" if name in words else "Bad person")
