# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# 05 listOverlap.py

import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

i = random.randint(0, 100)
j = random.randint(0, 100)

if i > j:
    a = random.sample(range(i), j)
    b = random.sample(range(i), j)
else:
    a = random.sample(range(j), i)
    b = random.sample(range(j), i)

a.sort()
b.sort()

print(a)
print(b)

print([x for x in set(a) if x in set(b)])
