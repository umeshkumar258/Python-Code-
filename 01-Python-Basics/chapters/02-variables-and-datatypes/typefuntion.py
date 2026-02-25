# Type Conversion Example

a = 84.48          # float value
b = "838"          # string value

try:
    converted_value = int(b)      # convert string to integer
    result = a + converted_value  # add float and int

    print(f"Converted value: {converted_value} (Type: {type(converted_value)})")
    print(f"Final result: {result} (Type: {type(result)})")

except ValueError:
    print("Error: Cannot convert string to integer.")
