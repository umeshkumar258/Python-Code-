# ---------------------------------------
# FUNCTION TO CHECK DIVISIBLE BY 5
# ---------------------------------------
def divisible_by_5(n):
    return n % 5 == 0


# Given list
a = [1, 2, 333, 45, 77, 7, 6665, 6663, 55, 65, 75]

# ---------------------------------------
# 1️⃣ Using filter() with function
# ---------------------------------------
result_filter = list(filter(divisible_by_5, a))
print("Divisible by 5 (filter + function):", result_filter)


# ---------------------------------------
# 2️⃣ Using lambda with filter()
# ---------------------------------------
result_lambda = list(filter(lambda x: x % 5 == 0, a))
print("Divisible by 5 (filter + lambda):", result_lambda)


# ---------------------------------------
# 3️⃣ Using list comprehension (MOST PYTHONIC)
# ---------------------------------------
result_comp = [x for x in a if x % 5 == 0]
print("Divisible by 5 (list comprehension):", result_comp)
