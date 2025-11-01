# Intialize imports (we'll be using random here)
import random

def setRandomNumber():
    return random.randint(0, 10)


def checkGuess(user, x):
    if user == x:
        return True
    else:
        return False

if __name__ == "__main__":
    x = setRandomNumber()
    while True:
        user = int(input("Guess a number 1-10: "))
        predict = checkGuess(user, x)

        if predict is True:
            print("Correct Guess! Good Job")
            break
        else:
            print("Incorrect! Try again")
    




