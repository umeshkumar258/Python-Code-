n = int(input("Enter the number: "))

def find_sum(n):
    if n == 1:
        return 1
    return find_sum(n - 1) + n

print("Sum =", find_sum(n))
