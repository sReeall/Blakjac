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
            self.value = tuple(int(rank))
        except: # must not be 1 - 10 rank
            # check if ace
            if rank != 'A' : self.value = (10)
            else: self.value = (1,11)

