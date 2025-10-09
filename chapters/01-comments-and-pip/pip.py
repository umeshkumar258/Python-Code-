# flask and django are modules 
# we have to use pip to install these modules 





import pyjokes    # it is an external module

print("Printing jokes")
print("getting jokes")
joke = pyjokes.get_joke()  # it is a function
print(joke)


# REPL read evluate print loop
# This is compund


from datetime import datetime, timedelta  

# Get the current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Create a custom date
custom_date = datetime(2024, 12, 7)
print(f"Custom date: {custom_date}")

# Add 5 days to the current date
new_date = now + timedelta(days=5)
print(f"Date after 5 days: {new_date}")

a = "umesh"
print(f"The name is :{a}")