# ── String Methods ─────────────────────────────────────────────
name = "harry"

# ── Introspection ──────────────────────────────────────────────
print(f"Original  : {name!r}")               # repr shows quotes → confirms it's a str
print(f"Type      : {type(name).__name__}")  # 'str' instead of <class 'str'>
print(f"Length    : {len(name)}")            # number of characters

# ── Case methods ───────────────────────────────────────────────
print(f"Upper     : {name.upper()}")         # "HARRY"
print(f"Lower     : {name.lower()}")         # "harry"
print(f"Capitalize: {name.capitalize()}")    # "Harry" — only first letter up

# ── Search & match ─────────────────────────────────────────────
print(f"find 'h'  : {name.find('h')}")       # index 0  — returns -1 if not found
print(f"find 'r'  : {name.find('r')}")       # index 2  — first occurrence only
print(f"count 'r' : {name.count('r')}")      # 2        — total occurrences

# ── Boolean checks ─────────────────────────────────────────────
print(f"starts 'h': {name.startswith('h')}") # True
print(f"ends 'ry' : {name.endswith('ry')}")  # True

# ── Transformation ─────────────────────────────────────────────
print(f"Replace   : {name.replace('harry', 'umesh')}")  # "umesh"
print(f"Original  : {name!r}")               # unchanged — strings are immutable
