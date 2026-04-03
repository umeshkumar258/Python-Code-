def main() -> None:
    print("--- 1. Creating a Set ---")
    numbers_set: set[int] = {37, 393, 283, 29, 66}
    
    # Using f-strings makes the output cleaner
    print(f"Set elements: {numbers_set}")
    print(f"Type of numbers_set: {type(numbers_set)}\n")


    print("--- 2. The 'Empty' Collection Gotcha ---")
    # It is better to compare the *empty* initialization of all data types
    empty_tuple: tuple = ()        
    empty_list: list = []        
    empty_string: str = ""       
    empty_dict: dict = {}        # Creates a Dictionary!
    empty_set: set = set()       # THIS is how you create an empty set

    print(f"Type of empty_dict {{}}: {type(empty_dict)}")
    print(f"Type of empty_set set(): {type(empty_set)}\n")


    print("--- 3. Demonstrating Set Properties ---")
    # 1️⃣ Sets are unordered (the print order may not match the creation order)
    unordered_set: set[int] = {10, 5, 20, 1}
    print(f"Unordered set: {unordered_set}")

    # 2️⃣ Sets automatically remove duplicate values
    # A common real-world trick is converting a list with duplicates into a set
    raw_list = [1, 2, 2, 3, 4, 4, 5]
    unique_set = set(raw_list)
    print(f"List converted to unique set: {unique_set}")

    # 3️⃣ Adding elements
    unique_set.add(6)
    print(f"After adding 6: {unique_set}")

    # 4️⃣ Removing elements (The Safe Way vs. The Strict Way)
    
    # .remove() throws a KeyError if the item doesn't exist
    unique_set.remove(3) 
    print(f"After strict removal of 3: {unique_set}")
    
    # .discard() removes the item, but silently does nothing if it's missing (safer!)
    unique_set.discard(999) 
    print(f"After safely discarding 999 (which wasn't there): {unique_set}")


if __name__ == "__main__":
    main()
