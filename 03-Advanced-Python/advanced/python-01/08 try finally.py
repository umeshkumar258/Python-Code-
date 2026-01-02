def main():
    try:
        # Taking input from the user
        a = int(input("Enter the number: "))
        
        # Printing the number if input is valid
        print("You entered:", a)
        
        # Return statement (function tries to exit)
        return

    except Exception as e:
        # This block executes if an error occurs
        print("Error:", e)
        
        # Return statement (function tries to exit)
        return

    finally:
        # This block ALWAYS executes
        # Even if return is present in try or except
        print("Finally block executed")

# Function call
main()
