
import random

def game():
    print("you are playing the game..")
    score = random.randint(1,59)
    # Fetch the hiscore

    with open("Hiscore.txt") as f:
        Hiscore  = f.read()
        if(Hiscore!=""):
            Hiscore = int(Hiscore)
        else:
            Hiscore = 0


    print(f"your score:{score}")
    if(score>Hiscore):
        # write this Hi socre to the file

        with open("Hiscore.txt","w") as f:
            f.write(str(score))

    return score



game()  # funcion call is very imp