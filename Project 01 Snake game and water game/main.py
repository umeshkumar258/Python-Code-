""""
1 for snake
-1 for water
0 for gun

"""
import random

computer = random.choice([-1,0,1])

youstr = input("Enter your choice :")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}

you = youDict[youstr]

# By now we have 2 number (variables), you and computer

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("it is Draw!")


if(computer == -1 and you ==1):
    print("You Win!")
elif(computer == -1 and you ==0):
    print("You Loose!")


if(computer == 1 and you ==0):
    print("You Win!")
elif(computer == 1 and you ==-1):
    print("You Loose!")


if(computer == 0 and you ==1):
    print("You Win!")
elif(computer == 0 and you ==-1):
    print("You Loose!")


