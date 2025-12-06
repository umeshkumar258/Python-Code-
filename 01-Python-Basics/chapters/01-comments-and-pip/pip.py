# Flask and Django are external Python frameworks
# We install such external modules using pip

import pyjokes  # external third-party module

print("Printing jokes...")
joke = pyjokes.get_joke()  # Fetch a random joke
print(f"Joke: {joke}")

# REPL = Read, Evaluate, Print, Loop
# Python terminal works as a REPL

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

# Example variable usage
name = "Umesh"
print(f"The name is: {name}")
