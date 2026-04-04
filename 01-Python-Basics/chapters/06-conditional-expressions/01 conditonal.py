def get_age():
    try:
        age = int(input("Enter your age: ").strip())
        
        if age <= 0:
            print("❌ Invalid age. Age must be greater than 0.")
        elif age < 18:
            print("🧒 You are a minor.")
        elif age == 18:
            print("🎉 You have just reached the age of consent.")
        else:
            print("✅ You are above the age of consent.")
    
    except ValueError:
        print("❌ Please enter a valid number.")

# Run the function
if __name__ == "__main__":
    get_age()
