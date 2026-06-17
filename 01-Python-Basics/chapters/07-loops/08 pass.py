# pass example
for i in range(5):
    pass

print("Pass does nothing.")
print()

# break example
i = 0

while i < 10:
    if i == 5:
        print("Break at", i)
        break

    print(i)
    i += 1
