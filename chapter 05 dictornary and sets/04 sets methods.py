# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values.


set = {37,393,283,29,66}

set2 = {35,72,283,9,66}

set.add(76)  # add an element to a set


set.difference(set2)

print(set.issubset(set2))

print(set.intersection(set2))

print(set.issuperset(set2))

print(set.union(set2))

print(set.remove(37))


print(len(set))


print(set)


# empty = set() # create an empty set

s1 = {1,2,3}
s2 = {1,2,3,4,6}

print(s2.issuperset(s1))