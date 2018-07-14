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
            self.value = int(rank)
        except: # must not be 2 - 10 rank
            # check if ace
            if rank != 'A' : self.value = 10,
            else: self.value = 1,11
    
    def __str__(self):
        return f'{self.rank}{self.suit}'
        
        
if __name__=='__main__':
    # test class card
    print('Create a card with suit H and rank J')
    card = card('H','J')
    print(card)
    print(card.value)
    

