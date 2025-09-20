import random


computer = random.randint(1,3)

dic = { 1: "gun ", 2 : "water", 3:"snake"}

user = int(input("Enter (1 for gun, 2 for water, 3 for snake): "))

if user not in [1, 2, 3]:
    print("Invalid input! Please enter 1, 2, or 3.")
else:
    print(f"Computer chose: {dic[computer]}")
    print(f"You chose: {dic[user]}")

    if computer == user:
        print("It's a tie!")
    elif (computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2):
        print("Computer wins!")
    else:
        print("You win!")