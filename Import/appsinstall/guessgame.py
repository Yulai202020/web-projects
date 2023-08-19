import random
def init():
    print("GuessGame ...")
    try:
        rand = random.randint(0,10)
        inp = int(input("Guess of number : "))
        if inp == rand:
            print("You win !!!")
        else :
            print("You lose ...")
            print("It's was : "+str(rand)+" ...")
    except:
        pass
