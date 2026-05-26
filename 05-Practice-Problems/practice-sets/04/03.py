# =========================================
#        TUPLE IMMUTABILITY DEMO
# =========================================

def tuple_immutability_demo():
    print("📘 Tuple Immutability Demo")
    print("-" * 35)

    # Creating a tuple
    numbers = (10, 20, 30)

    print("✅ Original Tuple :", numbers)

    # Trying to modify tuple element
    print("\n🔄 Trying to change numbers[0] = 100 ...")

    try:
        numbers[0] = 100   # Tuples are immutable
    except TypeError as error:
        print("❌ Error Occurred!")
        print("👉", error)

    # Tuple remains unchanged
    print("\n✅ Final Tuple (Unchanged) :", numbers)

    print("\n📌 Conclusion:")
    print("Tuples are immutable, meaning their values")
    print("cannot be changed after creation.")

# Function Call
tuple_immutability_demo()
