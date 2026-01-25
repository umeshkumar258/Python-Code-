def fahrenheit(celsius):
    return (celsius * 9/5) + 32


n = float(input("Enter the temperature in Celsius: "))

result = fahrenheit(n)
print("Temperature in Fahrenheit:", result)

print("Thanks")
