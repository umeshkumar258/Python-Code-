# -------- LIST & TUPLE PROGRAM --------

# List Part
marks = []

for i in range(4):
    m = int(input(f"Enter marks {i + 1}: "))
    marks.append(m)

marks.sort()

print("\nSorted Marks:", marks)
print("Sum of Marks:", sum(marks))

# Tuple Part
a = (7, 0, 8, 0, 0, 9)

print("\nTuple:", a)
print("Sum of Tuple:", sum(a))
print("Number of zeros:", a.count(0))
