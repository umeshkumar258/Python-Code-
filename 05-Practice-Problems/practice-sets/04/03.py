# -------- TUPLE IMMUTABILITY DEMO --------

t = (10, 20, 30)

print("Original tuple:", t)

# Trying to modify (will cause error)
try:
    t[0] = 100
except TypeError as e:
    print("❌ Error:", e)

print("Final tuple (unchanged):", t)
