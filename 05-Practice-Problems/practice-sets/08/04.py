def find_sum(n):
    if n <= 1:
        return n
    return n + find_sum(n - 1)


number = int(input("Enter the number: "))

print("Sum =", find_sum(number))
