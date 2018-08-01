'''
Created on 30 Jul 2018

@author: sReeall
'''
from Player import player
from Dealer import dealer
from os import system
from time import sleep

class table():
    #
    # class used to display game screens
    #
    
    def __init__(self,player,dealer):
        
        self.player = player
        self.dealer = dealer
    
    def displayBoard(self):
        
        print(f'Player: {self.player.getName()}')
        print(f'Current Balance: {self.player.getBalance()}')
        print('')
        print("|{:-^60}|".format(" Table "))
        print('|{:^30}'.format('') + '|'+ '{:^29}'.format('') +'|')
        
        # names
        
        print(f'| {self.player.getName():^29}| {self.dealer.getName():^28}|')
        print('|{:^30}'.format('') + '|'+ '{:^29}'.format('') +'|')
        print('|{:-^60}|'.format(''))        
        
        
        # hands
        
        if (self.player.getHand()).isEmpty(): 
            print('|{:^30}'.format('') + '|'+ '{:^29}'.format('') +'|')
        else: 
            print(f'| {str(self.player.getHand()):29}| {str(self.dealer.getHand()):28}|')
        print('|{:^30}'.format('') + '|'+ '{:^29}'.format('') +'|')
        
        playerHandValueStr = "Hand Value: " + str(self.player.hand.getvalue())
        
        if self.dealer.getIsTurn():
            dealerHandValuestr = "Hand Value: " + str(self.dealer.hand.getvalue())
        else: dealerHandValuestr = ''
        
        print(f'| {playerHandValueStr:29}| {dealerHandValuestr:28}|')
#        print('|{:^60}'.format('')+'|')
        print('|{:-^60}|'.format(''))
        print('Bet')
        print(f'{self.player.getBet()}')
        
        
    def clearScreen (self):
        
        system('cls')
        
    
     
if __name__=='__main__':
       
    testplayer = player('sunny')
    testdealer = dealer()
    testtable = table(testplayer,testdealer)
       
    testtable.displayBoard()
    
    print('clear screen in...3')
    
    sleep(1)
    
    print('2')
    
    sleep (1)
    
    print('1')
    
    sleep(1)
    
    testtable.clearScreen()
    
    sleep(3)
    
    testtable.displayBoard()