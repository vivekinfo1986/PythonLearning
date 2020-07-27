'''
#Create a program by using shuffle function and retrun the result
from random import shuffle
mylist = [12,3,9,56,8674,2]
def my_shuffle(mylist):
    shuffle(mylist)
    return mylist
result = my_shuffle(mylist)
print(result)
'''

#Create a program as a shuffle game which interact with functions
from random import shuffle
mylist = [' ', 'O', ' ']
shuffle(mylist)
def player_guess():
    guess = ''
    Choice = 'Y'
    if Choice == 'Y':
        while guess not in ['0', '1', '2']:
            guess = input('Guess 0, 1 or 2 ')
            player_guess_result(int(guess),mylist)

def player_guess_result(guess,mylist):
    if mylist[guess] == 'O':
        print('Your guess is correct')
        print(mylist)
    else:
        print('Better luck next time!!')
        print(mylist)
        choice = input('Do you want to play again (Y/N) ')
        if choice == 'Y':
            shuffle(mylist)
            player_guess()

player_guess()



