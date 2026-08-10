# Marks Sorting Program

def get_marks(count):
    marks = []

    for i in range(count):
        mark = int(input("Enter marks: "))

        while mark < 0 or mark > 100:
            print("Enter marks between 0 and 100!")
            mark = int(input("Enter marks: "))

        marks.append(mark)

    return marks


def display_marks(marks):
    print("\nMarks List:")

    for i, mark in enumerate(marks, start=1):
        print(i, mark)


def marks_sorting():

    print("Marks Sorting Program")
    print("---------------------")

    count = int(input("How many marks? "))

    marks = get_marks(count)

    # Original marks
    print("\nOriginal Marks:")
    display_marks(marks)

    # Sort marks
    sorted_marks = sorted(marks)

    print("\nSorted Marks:")
    display_marks(sorted_marks)

    # Statistics
    print("\nHighest:", max(marks))
    print("Lowest:", min(marks))
    print("Average:", sum(marks) / len(marks))


# Run program
if __name__ == "__main__":
    marks_sorting()
