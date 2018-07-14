'''
Created on 14 Jul 2018

@author: sReeall
'''

class card():
    
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
        
        
if __name__=='__main__':
    # test class card
    print('Create a card with suit H and rank J')
    card1 = card('H','J')
    print(card1)
    print(card1.value)
    
    print('Create a card with suit C and rank A')
    card2 = card('C','A')
    print(card2)
    print(card2.value)
    
    print('Ceate a card with suit D and rank 2')
    card3 = card('D','2')
    print(card3)
    print(card3.value)
    
