import random 

n = random.randint(1,20)

a = -1
guesses = 0

while(a != n):
    guesses +=1
    user = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")
    else:
        print("correcte number")


print(f"you have guessed the number correctly in {guesses} attempt")
