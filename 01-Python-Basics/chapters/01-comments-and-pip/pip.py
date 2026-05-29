# Author: Umesh Kumar J B

from datetime import datetime, timedelta
import pyjokes

# Print a random joke
print("Random Joke:")
print(pyjokes.get_joke())

# Current date and time
now = datetime.now()
print("\nCurrent Date & Time:", now)

# Custom date
custom_date = datetime(2024, 12, 7)
print("Custom Date:", custom_date)

# Date after 5 days
future_date = now + timedelta(days=5)
print("Date After 5 Days:", future_date)

print("\nKeep Learning Python! 🚀")
