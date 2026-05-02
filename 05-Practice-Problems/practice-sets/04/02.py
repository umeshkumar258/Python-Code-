# -------- IMPROVED MARKS SORTING PROGRAM --------

def get_marks(count):
    marks = []
    for i in range(count):
        while True:
            try:
                mark = int(input(f"Enter marks {i + 1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("⚠️ Enter marks between 0 and 100.")
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")
    return marks


def display_marks(marks):
    print("\n📋 Marks List:")
    for i, mark in enumerate(marks, start=1):
        print(f"{i}. {mark}")


def marks_sorting():
    print("📘 Marks Sorting Program")
    print("-" * 30)

    try:
        count = int(input("How many marks do you want to enter? "))
        if count <= 0:
            print("❌ Please enter a valid number.")
            return
    except ValueError:
        print("❌ Invalid input.")
        return

    marks = get_marks(count)

    print("\n🔹 Original Marks:")
    display_marks(marks)

    # Sorting
    sorted_marks = sorted(marks)

    print("\n🔹 Sorted Marks (Ascending):")
    display_marks(sorted_marks)

    print(f"\n📊 Highest Marks: {max(marks)}")
    print(f"📊 Lowest Marks: {min(marks)}")
    print(f"📊 Average Marks: {sum(marks)/len(marks):.2f}")


# Run program
if __name__ == "__main__":
    marks_sorting()
