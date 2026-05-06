def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius = float(input("Enter temperature in Celsius: "))

print("Temperature in Fahrenheit:", to_fahrenheit(celsius))
print("Thanks")
