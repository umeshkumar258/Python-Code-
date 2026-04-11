def print_number_range(start, end, step=1, label="Numbers"):
    """
    Prints a range of numbers with a descriptive label.
    """
    print(f"--- {label} ({start} to {end}) ---")
    
    # We use end + 1 because range is exclusive of the stop parameter
    for i in range(start, end + 1, step):
        print(i)

# 1. Print numbers 1 to 50
print_number_range(1, 50)

# 2. Print even numbers 2 to 10
# Using the default 'step' for the first call and overriding it here
print_number_range(2, 10, step=2, label="Even Numbers")
