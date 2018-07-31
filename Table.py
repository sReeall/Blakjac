'''
Created on 30 Jul 2018

@author: sReeall
'''
from Player import player
from Dealer import dealer

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
        print('|{:^60}'.format('')+'|')
        print(f'| {self.player.getName():29} {self.dealer.getName():29}|')
        print('|{:^60}'.format('')+'|')
        if (self.player.getHand()).isEmpty(): 
            print('|{:^60}'.format('')+'|')
        else: 
            print(f'| {str(self.player.getHand()):29} {str(self.dealer.getHand()):29}|')
        print('|{:^60}'.format('')+'|')
        print('|{:^60}'.format('')+'|')
        print('{:-^60}'.format(''))
        print('Bet')
        print(f'{self.player.getBet()}')
    def clearBoard(self):
        
        pass
    
     
if __name__=='__main__':
       
    testplayer = player('sunny')
    testdealer = dealer()
    testtable = table(testplayer,testdealer)
       
    testtable.displayBoard()