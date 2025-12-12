# --------------------------------
# Example 1: Using the pass keyword
# --------------------------------

# 'pass' is a placeholder. It does nothing.
# Useful when you want to write code later.
for i in range(22):
    pass   # Loop runs but does nothing


# --------------------------------
# Example 2: while loop with break
# --------------------------------

i = 0
while i < 20:
    if i == 11:
        print("Break triggered at i =", i)
        break   # Stops the loop immediately
    
    print(i)
    i += 1
