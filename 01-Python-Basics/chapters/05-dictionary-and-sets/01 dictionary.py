def display_marks(data):
    print(f"Dictionary: {data}")
    print(f"Type: {type(data)}")
    print(f"Length: {len(data)}")


def main():
    # Use integers for marks (not strings)
    marks = {
        "umesh": 73,
        "bab": 99,
        "harry": 72
    }

    display_marks(marks)

    # Accessing values safely
    print(f"Umesh's marks: {marks.get('umesh')}")
    print(f"Bab's marks: {marks.get('bab')}")

    # Safe access with default value
    print(f"John's marks (default if missing): {marks.get('john', 'Not Found')}")

    # Dictionary with list value
    student_data = {
        "numbers": [939, 9303, 99],
        "umesh": 939
    }

    print(f"\nStudent Data: {student_data}")
    print(f"Numbers list: {student_data['numbers']}")


if __name__ == "__main__":
    main()
