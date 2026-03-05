try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("❗ Invalid age entered. Age must be greater than 0.")

    elif age < 18:
        print("⚠️ You are not old enough.")

    elif age <= 98:
        print("🙂 You are doing good.")

    elif age == 99:
        print("🎉 Wow! You are 99 years old! Ok buddy.")

    else:
        print("👋 Welcome! You are above 99.")

except ValueError:
    print("❗ Please enter a valid number for age.")
