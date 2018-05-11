# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# 06 stringLists.py

print('Give me a string: ', end='')
string = input()

if string[::-1] == string:
    print('\'' + string + '\' is a palindrome.')
else:
    print('Sorry \'' + string + '\' is not a palindrome.')
