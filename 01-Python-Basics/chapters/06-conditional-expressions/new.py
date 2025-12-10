print("📌 Phone Number Validation Program")

# Step 1: Take input as string
phone = input("Enter your 10-digit phone number: ")

# Step 2: Validation
if phone.isdigit() and len(phone) == 10 and phone[0] in "6789":
    print("✔ Valid Indian phone number")
else:
    print("❌ Invalid phone number")
