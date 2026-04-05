# ── String Basics ──────────────────────────────────────────────
first_name = "Umesh"

# Slicing: extract first 3 characters
short_name = first_name[:3]

# Immutability: build a new string instead of modifying in place
modified_name = "U" + first_name[1:]

# Concatenation
combined_name = first_name + first_name  # duplicate_name was identical, so skip the alias

# ── Output ─────────────────────────────────────────────────────
print(f"Full name      : {first_name}")
print(f"Short name     : {short_name}")
print(f"Modified name  : {modified_name}")
print(f"Concatenated   : {combined_name}")
print(f"Type           : {type(first_name).__name__}")  # __name__ gives 'str' not <class 'str'>
