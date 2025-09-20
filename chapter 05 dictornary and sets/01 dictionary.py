a = { "umesh": "73", "bab":"99","harry":"72"}

print(type(a),a)


# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys.


print(a["umesh"])   #not allowed a[0] as it is unordered

print(len(a))

print(a["bab"])
print(a.get("bab"))     # both are same

list1 = {"numbers": [939, 9303, 99], "umesh": "939"}

print(list1)
print(list1["numbers"])