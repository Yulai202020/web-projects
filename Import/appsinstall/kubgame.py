import random
def init():
    print("Roll the dice ...")
    a = int(input("Guess number 0-6 # "))
    rand = random.randint(1,6)
    if a == rand:
        print("You win !!!")
    else:
        print(f"You lose !!!\nI's is {rand}")