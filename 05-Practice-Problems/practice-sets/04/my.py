# -------- LIST & TUPLE PRACTICE PROGRAM --------

def list_and_tuple_demo():
    print("📘 LIST & TUPLE PRACTICE")
    print("=" * 35)

    # -------- LIST: MARKS --------
    marks = []

    for i in range(4):
        m = int(input(f"Enter marks {i+1}: "))
        marks.append(m)

    marks.sort()

    print("\n📋 Sorted Marks:", marks)
    print("➕ Sum of Marks:", sum(marks))

    # -------- TUPLE --------
    a = (7, 0, 8, 0, 0, 9)

    zero_count = a.count(0)
    total_sum = sum(a)

    print("\n📘 Tuple:", a)
    print("➕ Sum of tuple elements:", total_sum)
    print("🔢 Number of zeros:", zero_count)

# Function call
list_and_tuple_demo()
