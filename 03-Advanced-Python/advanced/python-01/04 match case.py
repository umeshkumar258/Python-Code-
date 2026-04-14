# Python Match-Case & Dictionary Merge - Improved Version

# -------------------------------
# 1. MATCH-CASE EXAMPLE
# -------------------------------
def http_status(status: int) -> str:
    match status:
        case 200:
            return "✅ OK"
        case 404:
            return "❌ Not Found"
        case 500:
            return "💥 Internal Server Error"
        case int() if 100 <= status < 600:
            return f"ℹ️ Other HTTP Status: {status}"
        case _:
            return "⚠️ Invalid Status Code"


print("🌐 HTTP Status Results:")
for code in [200, 404, 500, 302, 66]:
    print(f"{code} → {http_status(code)}")


# -------------------------------
# 2. DICTIONARY MERGE
# -------------------------------
dict1: dict[str, int] = {"a": 4, "b": 9}
dict2: dict[str, int] = {"c": 88, "d": 99}

merged: dict[str, int] = dict1 | dict2

print("\n📌 Merged Dictionary:")
print(merged)


# -------------------------------
# 3. MERGE WITH SAME KEY
# -------------------------------
dict3: dict[str, int] = {"a": 100, "e": 50}
merged2: dict[str, int] = dict1 | dict3

print("\n📌 Merged with same key (right wins):")
print(merged2)


# -------------------------------
# 4. SAFE MERGE (WITHOUT OVERWRITE)
# -------------------------------
safe_merge = dict1.copy()

for key, value in dict3.items():
    if key not in safe_merge:
        safe_merge[key] = value

print("\n🔐 Safe Merge (no overwrite):")
print(safe_merge)


print("\n✅ Program ended successfully")
