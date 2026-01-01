# -----------------------------------
# EXCEPTION HANDLING - ALL IN ONE
# -----------------------------------

def get_number():
    try:
        # Risky code
        a = int(input("Hey, enter a number: "))
        print("You entered:", a)

    except ValueError as v:
        # Handles wrong input type
        print("Invalid input! Enter only numbers.")
        print("Error:", v)

    except Exception as e:
        # Handles all other errors
        print("Unexpected error:", e)

    else:
        # Executes if no exception occurs
        print("Conversion successful.")

    finally:
        # Always executes
        print("Thanks for using the program.\n")


# Function call
get_number()
