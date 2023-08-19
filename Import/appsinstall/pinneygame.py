import random
def init():
    print("PinneyGame ...")
    try:
        rand = random.randint(0,1)
        inp = input("Heads or tails : ")
        if inp == "heads":
            if rand == 0:
                print("You win !!!")
            else:
                print("You lose ...")
        elif inp == "tails" :
            if rand == 1:
                print("You win !!!")
            else:
                print("You lose ...")
    except:
        pass
# info
