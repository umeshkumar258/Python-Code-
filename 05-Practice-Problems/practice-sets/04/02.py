# -------- MARKS SORTING PROGRAM --------

def marks_sorting():
    marks = []

    print("📘 Marks Sorting Program")
    print("-" * 30)

    for i in range(5):
        mark = int(input(f"Enter marks {i+1}: "))
        marks.append(mark)

    print("\nOriginal Marks List:")
    print(marks)

    # Sorting the list
    marks.sort()

    print("\nSorted Marks List:")
    print(marks)

# Function call
marks_sorting()
