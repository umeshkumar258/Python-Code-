import random


user = int(input("Guess the Number :"))

computer = random.randint(1,20)
print(f"computer number: {computer}")

print(f"user number:{user}")

if (user>computer):
    print("You guess the higher numeber")

elif (computer>user):
    print("you guess the lower number")


else:
    print("you guess the correct number")