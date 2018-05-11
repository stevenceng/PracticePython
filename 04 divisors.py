# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# 4 divisors.py

number = int(input('Give me a number: '))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)
