# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# 08 rockPaperScissors.py

while True:
    print('Rock, Paper, and Scissors')
    print('\'q\' to quit')

    print('Player One: ', end='')
    one = input().lower()
    if one == 'q':
        break

    print('Player Two: ', end='')
    two = input().lower()
    if two == 'q':
          break

    if one == 'rock' and two == 'scissors':
        print('Player One wins! Rock beats scissors.')
    elif one == 'rock' and two == 'paper':
        print('Player Two wins! Paper beats rock.')
    elif one == 'scissors' and two == 'rock':
        print('Player Two wins! Rock beats scissors.')
    elif one == 'scissors' and two == 'paper':
        print('Player One wins! Scissors beats paper.')
    elif one == 'paper' and two == 'rock':
        print('Player One wins! Paper beats rock.')
    elif one == 'paper' and two == 'scissors':
        print('Player two wins! Scissors beats paper.')
    else:
        print('It\'s a tie! Both players played ' + one + '.')

    print('')
