# ── String Slicing ─────────────────────────────────────────────
name = "umesh"
#       u  m  e  s  h
#       0  1  2  3  4   (positive indices)
#      -5 -4 -3 -2 -1   (negative indices)

# ── Basic slicing [start:stop] ─────────────────────────────────
print(name[1:])          # "mesh"  — from index 1 to end
print(name[-4:])         # "mesh"  — same result via negative index
print(name[-5:])         # "umesh" — full string from negative start
print(name[-1:])         # "h"     — last character as a slice

# ── Step slicing [start:stop:step] ────────────────────────────
print(name[0::2])        # "ueh"   — every 2nd char (indices 0, 2, 4)
print(name[0::4])        # "uh"    — every 4th char (indices 0, 4)

# ── Negative index slicing ─────────────────────────────────────
print(name[-2:])         # "sh"    — last 2 characters
print(name[-2:-1])       # "s"     — second-to-last only
print(name[1:2])         # "m"     — single char via range (vs name[1])

# ── Reverse ────────────────────────────────────────────────────
print(name[::-1])        # "hsemu" — step of -1 walks backwards
