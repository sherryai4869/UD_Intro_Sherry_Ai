import random
a = input("please choose a number: ")
b = input("please choose another number: ")
randomNumber = random.randint(int(a),int(b))

while True:
    guessNumber = input("please guess a number: ")
    guessNumber = int(guessNumber)
    if guessNumber == randomNumber:
        print('congratulations, you make it right!')
        break

    else:
        print('sorry, please try again!')