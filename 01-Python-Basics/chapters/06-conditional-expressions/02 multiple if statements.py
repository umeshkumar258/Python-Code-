age = int(input("Enter your age: "))

if age <= 0:
    print("❗ Invalid age entered.")

elif age < 18:
    print("⚠️ You are not old enough.")

elif age < 99:
    print("🙂 You are doing good.")

elif age == 99:
    print("🎉 Wow! You are 99 years old! Ok buddy.")

else:
    print("👋 Welcome! You are above 99.")
