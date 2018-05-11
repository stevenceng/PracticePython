# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# 09 Guessing Game One

import random
number = random.randint(1, 9)


print('I generated a number between 1 and 9. Please guess what it is: ', end='')

guess = input()

numberOfGuess = 0

while guess != number:
    if guess > number:
        print('Your guess is too high!')
    elif guess < number:
        print('Your guess is too low!')
    numberOfGuess = numberOfGuess + 1

p
