def main():
    # Use integers for marks
    marks = {
        "umesh": 73,
        "babu": 87,
        "harry": 88
    }

    # Display items
    print(f"Items: {list(marks.items())}")
    print(f"Keys: {list(marks.keys())}")
    print(f"Values: {list(marks.values())}")
    print(f"Number of students: {len(marks)}")

    # Safe access
    print(f"Umesh's marks (before update): {marks.get('umesh')}")

    # Updating existing key
    marks.update({"umesh": 89})

    # Adding new key
    marks["vinay"] = 99

    # Removing key safely
    removed = marks.pop("umesh", None)
    print(f"Removed value: {removed}")

    print(f"Updated dictionary: {marks}")

    # Safe access
    print(f"Unknown key: {marks.get('umesh4', 'Not Found')}")


if __name__ == "__main__":
    main()
