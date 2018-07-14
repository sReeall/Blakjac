'''
Created on 14 Jul 2018

@author: sReeall
'''

class card():
    '''
    used to represent a single card and is basic component of deck class.
    
    constructor:
        suit
        rank
    
    attributes:
        suit: should be one of the following 'H', 'C', 'D', 'S'
        rank: 2 - 10, 'J', 'Q', 'K', 'A'
        value: tuple used as rank 'A' has 1 and 11
        
    '''
    def __init__ (self,suit,rank):
        self.suit = suit
        self.rank = rank
        
        # values assigned automatically based on rank
        try: # add cast to int
            self.value = int(rank),
        except: # must not be 2 - 10 rank
            # check if ace
            if rank != 'A' : self.value = 10,
            else: self.value = 1,11
    
    def __str__(self):
        return f'{self.rank}{self.suit}'
        
class deck():
    '''
    represents a deck of 52 card
    can contain multiples 52 cards if num is specified.
    
    
    '''
    def __init__(self,num=1):
        
        pass
    
    
    
if __name__=='__main__':
    # test class card
#     print('Create a card with suit H and rank J')
#     card1 = card('H','J')
#     print(card1)
#     print(card1.value)
#     
#     print('Create a card with suit C and rank A')
#     card2 = card('C','A')
#     print(card2)
#     print(card2.value)
#     
#     print('Ceate a card with suit D and rank 2')
#     card3 = card('D','2')
#     print(card3)
#     print(card3.value)
    
