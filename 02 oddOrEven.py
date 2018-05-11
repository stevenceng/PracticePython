# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# 2 oddOrEven.py

number = input('Pick a number: ')

if int(number) % 4 == 0:
    print(number + ' is a multiple of 4 and an even number.')
elif int(number) % 2 == 0:
    print(number + ' is an even number.')
else:
    print(number + ' is an odd number.')
print('')

check = input('Pick a number: ')
num = input('Pick a second number: ')

if int(num) % int(check) == 0:
    print(check + ' divides evenly into ' + num)
else:
    print(check + ' does not divide evenly into ' + num)
