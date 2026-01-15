# ---------- SET CREATION ----------
print("---- SET CREATION ----")

s = set()
print("Empty set:", s)
print("Type:", type(s))

print("\n---- ADDING ELEMENTS ----")

# Adding integer
s.add(20)
print("After adding 20:", s)

# Adding float (same value as 20)
s.add(20.0)
print("After adding 20.0:", s)

# Adding string
s.add('20')
print("After adding '20':", s)

print("\n---- FINAL SET ----")
print("Final set:", s)
print("Length of set:", len(s))

print("\n---- WHY THIS HAPPENS ----")
print("20 == 20.0 ->", 20 == 20.0)
print("Type of 20:", type(20))
print("
