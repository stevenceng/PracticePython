# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# 07 listComprehensions.py

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([x for x in a if x % 2 == 0])
