import random
randomNumber = random.randint(1,20)

while True:
    guessNumber = input("please guess a number between 1 and 20: ")
    guessNumber = int(guessNumber)
    if guessNumber == randomNumber:
        print('congratulations, you make it right!')
        break

    else:
        print('sorry, please try again!')