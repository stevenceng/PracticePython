# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# 3 listLessThanTen.py

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)

print('')

# Extra 1
b = []
for i in a:
    if i < 5:	
        b.append(i)

print(b)
print('')

# Extra 2
print([x for x in a if x < 5])
print('')

# Extra 3

num = input('Give me a number: ')
print('These are the numbers smaller than ' + num + ': ' + str([x for x in a if x < int(num)]))
