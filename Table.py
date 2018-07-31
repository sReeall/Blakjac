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
        print('------\t Table\t ------')
        print('')
        print(f'{self.player.getName():20} {self.dealer.getName()}')
        print('')
        print(f'{str(self.player.getHand()):20} {self.dealer.getHand()}')
        print('')
        print('')
        print('Bet')
        print(f'{self.player.getBet()}')
    def clearBoard(self):
        
        pass
    
     
# if __name__=='__main__':
#       
#     testplayer = player('sunny')
#     testdealer = dealer()
#     testtable = table(testplayer,testdealer)
#       
#     testtable.displayBoard()