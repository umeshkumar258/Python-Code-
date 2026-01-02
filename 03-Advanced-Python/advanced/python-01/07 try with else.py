try:
    # Taking input from the user and converting it to integer
    a = int(input("Hey, enter a number: "))
    
    # If conversion is successful, print the number
    print("You entered:", a)

except Exception as e:
    # This block executes if any error occurs in try block
    print("Error occurred:", e)

else:
    # This block executes only when no exception occurs
    print("I am inside else block (No error occurred)")

finally:
    # This block executes whether error occurs or not
    print("Program execution completed")
