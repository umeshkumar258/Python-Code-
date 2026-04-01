def show(step, lst):
    print(f"{step:<30} -> {lst}")  # aligned output


def main():
    a = [3, 5, 7, 88, 46]
    show("Original", a)

    # Sorted copy (without modifying original)
    sorted_list = sorted(a)
    show("Sorted (new list)", sorted_list)

    # Reverse copy
    reversed_list = list(reversed(a))
    show("Reversed (new list)", reversed_list)

    # In-place operations
    print("\n🔹 In-place Operations")

    a.sort()
    show("Sorted (in-place)", a)

    a.append(88)
    show("Append 88", a)

    a.insert(3, 99)
    show("Insert 99 at index 3", a)

    removed_value = a.pop(2)
    show(f"Pop index 2 (removed {removed_value})", a)

    # Searching
    print("\n🔹 Searching & Counting")

    try:
        index_88 = a.index(88)
        print(f"Index of first 88        -> {index_88}")
    except ValueError:
        print("88 not found")

    print(f"Count of 88             -> {a.count(88)}")

    show("Final list", a)


if __name__ == "__main__":
    main()
