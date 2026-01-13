# -------- SET INPUT PROGRAM --------

def set_demo():
    s = set()

    print("📘 Set Program (Unique Numbers)")
    print("-" * 35)

    for i in range(5):
        n = int(input(f"Enter number {i+1}: "))
        s.add(n)

    print("\n📋 Set Elements:")
    print(s)

# Function call
set_demo()
