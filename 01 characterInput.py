# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# 01 characterInput.py

name = input('What is your name? ')
age = input('What is your age? ')
print('You will turn 100 years old in ' +  str(100- int(age) + 2018) + '.\n')

loop = int(input('Feed me another number: '))

print('Printing previous string ' + str(loop) + ' times.\n')

for i in range(loop):
    print('You will turn 100 years old in the year ' +  str(100 - int(age) + 2018) + '.')
print('')
