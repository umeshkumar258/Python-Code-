def find_sum(n):
    if n <= 1:
        return n
    return n + find_sum(n - 1)


number = int(input("Enter the number: "))
result = find_sum(number)

print("Sum =", result)
