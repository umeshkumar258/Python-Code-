def main() -> None:
    # 1. Type hinting makes the expected data types clear
    marks: dict[str, int] = {
        "umesh": 73,
        "babu": 87,
        "harry": 88
    }

    print("--- Initial Dictionary Information ---")
    # 2. Raw lists are hard to read; loops and string joins provide better output formatting
    print(f"Number of students: {len(marks)}")
    print(f"Students: {', '.join(marks.keys()).title()}")
    print(f"Scores: {list(marks.values())}")

    print("\n--- Safe Access & Updates ---")
    print(f"Umesh's marks (before update): {marks.get('umesh')}")

    # 3. Direct assignment is more idiomatic for updating a single key than .update()
    marks["umesh"] = 89 
    
    # Adding a new key uses the exact same syntax
    marks["vinay"] = 99  
    print("Added Vinay and updated Umesh.")

    print("\n--- Removals ---")
    # Removing key safely
    student_to_remove = "umesh"
    removed_score = marks.pop(student_to_remove, None)
    
    # 4. Adding conditional logic makes the output more informative
    if removed_score is not None:
        print(f"Successfully removed {student_to_remove.capitalize()} (Score: {removed_score})")
    else:
        print(f"Could not remove {student_to_remove.capitalize()} - not found.")

    print("\n--- Final Roster ---")
    # 5. Iterating through items creates a much cleaner final display
    for student, score in marks.items():
        print(f"{student.capitalize()}: {score}")

    print("\n--- Edge Cases ---")
    # Safe access with a custom fallback message
    print(f"Looking for 'umesh4': {marks.get('umesh4', 'Not Found')}")


if __name__ == "__main__":
    main()
