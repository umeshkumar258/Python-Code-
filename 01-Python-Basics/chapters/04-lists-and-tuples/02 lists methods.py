def show(step, lst):
    print(f"{step}: {lst}")

a = [3, 5, 7, 88, 46]
show("Original", a)

# Sorted copy (without modifying original)
sorted_list = sorted(a)
show("Sorted (new list)", sorted_list)

# Reverse copy
reversed_list = list(reversed(a))
show("Reversed (new list)", reversed_list)

# Continue modifying original
a.sort()
show("Sorted (in-place)", a)

a.append(88)
show("Append 88", a)

a.insert(3, 99)
show("Insert 99 at index 3", a)

removed_value = a.pop(2)
show(f"Pop index 2 (removed {removed_value})", a)

if 88 in a:
    print("Index of first 88:", a.index(88))
else:
    print("88 not found")

print("Count of 88:", a.count(88))

show("Final list", a)
