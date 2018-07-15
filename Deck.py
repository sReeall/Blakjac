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
    can contain multiples 52 cards if num is specified (not implimented yet)
    
    attributes:
        cards - list of 52 cards as found in a deck
        
    methods:
        suffle - mix up the cards
        
    '''
    def __init__(self,num=1):
        '''
        constructor setups an list of card objects called cards 
        '''
        
        # setup hearts
        hearts = [card]*13
        
        # setup ace
        hearts[0] = card('H','A')
        
        #setup 2 - 10 cards
        for i in range(1,10):
            hearts[i] = card('H',i+1)
        
        # setup jack, queen and king 
        hearts[10] = card('H','J')
        hearts[11] = card('H','Q')
        hearts[12] = card('H','K')
            
        # setup diamonds
        dia = [card]*13
    
        # setup ace
        dia[0] = card('D','A')
        
        #setup 2 - 10 cards
        for i in range(1,10):
            dia[i] = card('D',i+1)
        
        # setup jack, queen and king 
        dia[10] = card('D','J')
        dia[11] = card('D','Q')
        dia[12] = card('D','K')
        
        # setup clubs
        club = [card]*13
    
        # setup ace
        club[0] = card('C','A')
        
        #setup 2 - 10 cards
        for i in range(1,10):
            club[i] = card('C',i+1)
        
        # setup jack, queen and king 
        club[10] = card('C','J')
        club[11] = card('C','Q')
        club[12] = card('C','K')

        # setup spades
        spade = [card]*13
    
        # setup ace
        spade[0] = card('S','A')
        
        #setup 2 - 10 cards
        for i in range(1,10):
            spade[i] = card('S',i+1)
        
        # setup jack, queen and king 
        spade[10] = card('S','J')
        spade[11] = card('S','Q')
        spade[12] = card('S','K')

        self.cards = hearts + dia + club + spade
        

if __name__=='__main__':
    pass
    # test class deck
#     mydeck = deck()
# 
#     for i in mydeck.cards:
#         print(i)
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