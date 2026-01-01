# -------------------------------
# MATCH-CASE EXAMPLE
# -------------------------------
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"


print("HTTP Status Results:")
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(66))


# -------------------------------
# DICTIONARY MERGE
# -------------------------------
dict1 = {"a": 4, "b": 9}
dict2 = {"c": 88, "d": 99}

merged = dict1 | dict2

print("\nMerged Dictionary:")
print(merged)


# -------------------------------
# EXTRA: MERGE WITH SAME KEY
# -------------------------------
dict3 = {"a": 100, "e": 50}
merged2 = dict1 | dict3

print("\nMerged with same key:")
print(merged2)
