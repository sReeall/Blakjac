'''
A hand consists of two cards initially, more can be added if the assigned player selects hit,
and the value is not greater then 21.
it is assigned to a player. if it is the dealer, only one card is visable.
it will need to be compared to other hands to check if it is winning.
if it totals 21, it is considered black jack.

Created on 15 Jul 2018

@author: sReeall
'''
from Deck import deck

class hand ():
    
    '''
    use to represent a hand 
    
    attr:
        list of cards
        owner - who the hand is assigned to
        containsAce - boolean, true if contains ace
        
    
    methods:
        addcard()- add a card to the list in the hand
        getvalue() - returns the sum of the list of cards. 
                     needs to take into consideration of aces
    '''
    
    def __init__(self):
        self.cards = []
        self.containsAce = False
        self.numAces = 0
        self.isBust = False
        self.isblackjack = False
        
    def getcard(self,num):
        return self.cards[num]

    def addcard(self,card):
        
        # check if card is ace
        if card.isAce(): 
            self.containsAce = True
            self.numAces += 1
        
        self.cards.append(card)
    
    def getvalue(self):
        
        value = 0 
        for card in self.cards:

            value = value + card.value[0]
        
        # we need to check if ace should be high or low
        # if we have bust, set ace to low by removing 10 from value        
        if value > 21 and self.containsAce: 
            for i in range(self.numAces): # takes card of multiple aces one at a time
                value = value - 10
                if value <= 21: break # dont need to process any more aces if value <= 21
            
        # if value of hand is still > 21 and we have set all aces to 1, we ha busted
        
        if value > 21: self.isBust = True
        if value == 21: self.isblackjack = True
            
        return value
    
    def __str__(self):
        strcards = ''
        for i in self.cards:
            strcards += str(i) + ' '
        return strcards
        
# if __name__=='__main__':
#     
#     myhand = hand()
#     mydeck = deck()
#     # shuffle the deck
#     mydeck.shuffe()
#        
#     for i in range(0,10):
# 
#         #peek at the top card
#         print(f'Top card in the deck is {mydeck.cards[-1]}')
#         # deal one card from the deck
#         myhand.addcard(mydeck.nextcard())
#         
#         print('Adding to hand')
#         
#         print(f'myhand is {myhand}')
#         
#         if myhand.containsAce: print(f"myhand contains {myhand.numAces} ace")
# 
#         
#         print(f"the value of my hand is {myhand.getvalue()}")
#         
#         if myhand.isblackjack: 
#             print("My hand is Black Jack!")
#             print("")
#             break
#         
#         if myhand.isBust: 
#             print("My hand is bust!")
#             print("")
#             break
#         
#         print("")