def show(step, lst):
    print(f"{step}: {lst}")

a = [3, 5, 7, 88, 46]
show("Original", a)

a.sort()
show("Sorted", a)

a.reverse()
show("Reversed", a)

a.append(88)
show("Append 88", a)

a.insert(3, 99)
show("Insert 99 at index 3", a)

a.pop(2)
show("Pop index 2", a)

a.remove(88)
show("Remove 88", a)

if 88 in a:
    print("Index of 88:", a.index(88))
else:
    print("88 not found")

print("Count of 88:", a.count(88))

show("Final list", a)
