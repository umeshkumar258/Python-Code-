a, d, c = [int(input("Enter your number: ")) for _ in range(3)]

average = (a + d + c) / 3

if average > 40:
    print("He scores good")
elif average > 33:
    print("He is pass")
else:
    print("Fail")
