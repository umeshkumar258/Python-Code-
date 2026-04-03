def main() -> None:
    print("--- 1. Initializing Sets ---")
    # Using type hints for clarity
    set1: set[int] = {37, 393, 283, 29, 66}
    set2: set[int] = {35, 72, 283, 9, 66}

    print(f"Set1: {set1}")
    print(f"Set2: {set2}")

    print("\n--- 2. Adding Elements ---")
    set1.add(76)
    print(f"After adding 76 to set1: {set1}")

    print("\n--- 3. Set Operations (Methods vs. Operators) ---")
    # You can use methods, but the symbolic operators are much more Pythonic!
    
    
    
    # INTERSECTION: Elements in BOTH sets
    print(f"Intersection (Method): {set1.intersection(set2)}")
    print(f"Intersection (Operator '&'): {set1 & set2}")

    # UNION: All unique elements combined
    print(f"Union (Method): {set1.union(set2)}")
    print(f"Union (Operator '|'): {set1 | set2}")
    
    # BONUS - DIFFERENCE: Elements in Set1 but NOT in Set2
    print(f"Difference (Operator '-'): {set1 - set2}")

    print("\n--- 4. Subsets & Supersets ---")
    s1: set[int] = {1, 2, 3}
    s2: set[int] = {1, 2, 3, 4, 6}
    
    print(f"s1: {s1}")
    print(f"s2: {s2}")
    
    # Using methods
    print(f"Is s1 a subset of s2? {s1.issubset(s2)}")
    print(f"Is s2 a superset of s1? {s2.issuperset(s1)}")
    
    # Using operators (<= for subset, >= for superset)
    print(f"Is s2 a superset of s1? (Operator '>='): {s2 >= s1}")

    print("\n--- 5. Removing Elements & Length ---")
    # Reinforcing our previous lesson: .discard() is safer than .remove()!
    set1.discard(37) 
    print(f"After safely discarding 37 from set1: {set1}")
    print(f"Length of set1: {len(set1)}")


if __name__ == "__main__":
    main()
