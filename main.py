import random
def guess(x):

    randomNum = random.randint(1,x)
    guess = 0

    while guess != randomNum:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNum:
            print('Sorry, guess again. Too low')
        elif guess > randomNum:
            print('Sorry, guess again. Too high.')

    print(f'Yay, you guessed the number {randomNum}')
guess(30)