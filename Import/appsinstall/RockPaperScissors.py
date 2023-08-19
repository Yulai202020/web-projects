import random
def init():
    abc = input("Rock,paper,scissors # ")
    rand = random.randint(0,2)
    if abc == "rock":
        if rand == 0:
            print("You win !!!")
        else :
            if rand == 1:
                print("You lose ...\nI's scissors ...")
            else :
                print("You lose ...\nI's paper ...")
    elif abc == "paper":
        if rand == 1:
            print("You win !!!")
        else :
            if rand == 0:
                print("You lose ...\nI's rock ...")
            else :
                print("You lose ...\nI's scissors ...")
    elif abc == "scissors":
        if rand == 2:
            print("You win !!!")
        else :
            if rand == 1:
                print("You lose ...\nI's paper ...")
            else :
                print("You lose ...\nI's rock ...")