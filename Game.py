'''
Created on 29 Jul 2018

@author: sReeall
'''
from Player import player

print('Welcome to BlakJac')

print('')
# Setup player and dealer

player1name = input('Please enter your name: ')

player1 = player(player1name)

while True:
    try:
        deposit = int(input('How much would you like to deposit?:'))
        break
    except:
        print('Oops! deposit needs to be a number. Please try again')

player1.setBalance(deposit)

print(f'Welcome {player1.getName()} your balance is now {player1.getBalance()}')

while True:
    startgame = str(input('Are you to start?[y/n]'))
    if startgame.lower() == 'y': break
    elif startgame.lower() == 'n': 
        print('Ok we will wait!')
    else: print('Oops! You need to enter y or n')


    