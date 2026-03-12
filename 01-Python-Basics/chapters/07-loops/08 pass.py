# ---------------------------------------
# Example 1: pass keyword
# ---------------------------------------

def pass_example():
    print("\n--- Pass Example ---")
    
    # Loop runs but does nothing
    for i in range(22):
        pass
    
    print("Loop executed, but 'pass' did nothing.")


# ---------------------------------------
# Example 2: while loop with break
# ---------------------------------------

def while_break_example():
    print("\n--- While Loop with Break ---")

    i = 0

    while i < 20:
        if i == 11:
            print(f"Break triggered at i = {i}")
            break

        print(i)
        i += 1


# ---------------------------------------
# Run the examples
# ---------------------------------------

pass_example()
while_break_example()
