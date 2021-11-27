
# ------------------------------------------------- #
# Title: Assingment 07
# Description: A simple example of storing data in a binary file
# ChangeLog: (Nick Soldano, 11/27/2021, File Created)
# <Nick Soldano>,<11.27.2021>,Created Script
# ------------------------------------------------- #
# This is an example of a exception handling program

# Data -------------------------------------------- #

class GuessError(Exception):
    def __init__(self, message):
        self.message = message
a = int(input('Enter the input : '))
try:
    if a < 3:
        raise GuessError('Your guess is wrong. Number is less.')
    elif a > 3:
        raise GuessError('Your guess is wrong. Number is high.')
    else:
        print('Your guess is right. The value is : {}.'.format(a))
except GuessError as e:
    print(e.message)