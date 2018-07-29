'''
Created on 29 Jul 2018

@author: sReeall
'''

from Player import player

class dealer(player):
    
    
    def __init__ (self):
        
        super().__init__(self, "Dealer", 0)
        
        self.isTurn = False

    def getOneCard(self):
        #deal needs to be able to return just one card when it is not his turn
        self.hand[0]

    def getHand(self):
        # dealer need to hide one card in the hand if it is not his turn
        
        if self.isTurn: return player.getHand(self)
            
        else: return self.getOneCard()