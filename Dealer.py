'''
Created on 29 Jul 2018

@author: sReeall
'''

from Player import player


class dealer(player):
    
    
    def __init__ (self):
        
        super().__init__("Dealer", 0)
        
        self.isTurn = False

    
    def getIsTurn(self):
        
        return self.isTurn
    
    def setIsTurn(self,value):
        
        self.isTurn = value

    def getOneCard(self):
        #deal needs to be able to return just one card when it is not his turn
        return str(self.hand.getcard(0)) + " XX"

    def getHand(self):
        # dealer need to hide one card in the hand if it is not his turn
        
        if self.isTurn: return player.getHand(self)
            
        else: return self.getOneCard()
    
    def __str__(self):
        return "hello I'm the dealer"    
        
# if __name__ == '__main__':
# 
#     testdeck = deck()
#     
#     testdeck.shuffe()
#     
#     testDealer = dealer()
#     
#     print(testDealer) 
# 
#     # deal cards to dealer
#     
#     print(f'dealing card to {testDealer.getName()}')
#     testDealer.hit(testdeck)
#     testDealer.hit(testdeck)
#      
#     print(f"{testDealer.getName()} has the folloiwng hand {testDealer.getHand()}")
#      
#     print('Setting to dealers turn')
#     
#     testDealer.setIsTurn(True)
#     
#     if testDealer.getIsTurn() : 
#         print('Its the dealers turn, we can not show both cards')
#         print(f"{testDealer.getName()} has the folloiwng hand {testDealer.getHand()}")
        