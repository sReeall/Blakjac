'''
Created on 21 Jul 2018

@author: sande
'''
from Hand import hand
from Deck import deck

class player():
    

    def __init__ (self, name, deposit = 0):
        
        self.name = name
        self.balance = deposit
        self.hand = hand()
    
    def placeBet (self,bet):
        
        # need to make sure there is enough in the balance
        # remove that amount from the players balance
        # return the amount bet
        if self.balance - bet >=0:
            self.balance = self.balance - bet
            return True
        else:
            return False
    
    def addChips (self,ammount):
        self.balance = self.balance + ammount
    
    def getBalance(self):
        return self.balance
    
    def getHand(self):
        return self.hand
    
    def getName(self):
        return self.name
    
    def hit(self,deck):
        
        # takes card from deck and adds to players hand
        # calls Deck.nextcard to get the top card
        
        self.hand.addcard(deck.nextcard())
        
    def __str__(self):
        return self.getName() + ' has ' + str(self.getBalance()) + ' chips'
    


if __name__ == '__main__':
    # testing player class
    
    testdeck = deck()
    
    testdeck.shuffe()
    
    testplayer = player("sunny",100)
    
    print(testplayer)