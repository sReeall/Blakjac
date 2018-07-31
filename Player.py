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
        self.bet = 0

    def clearBet(self):
        self.bet = 0
        
    def placeBet (self):
        
        # need to make sure there is enough in the balance
        # remove that amount from the players balance
        # return the amount bet
        
        while True:
        
            try: 
                bet = int(input(f'{self.getName()} how much would you like to bet?'))
            except:
                print('Please enter a number!')
                continue
            
            if bet == 0:
                print('This is gambling, you cant bet nothing :)')
                continue
            
            if bet < 0 :
                print('Cannot bet a negative amount')
                continue
               
            if (self.getBalance() - bet) >= 0 :
                self.setBalance(self.getBalance() - bet)
                self.bet = bet
                break
            
            else :
                print(f'your balance of {self.getBalance()} is too low for that bet')

        return bet
    
    def getBet(self):
        return self.bet
    
    def addChips (self,ammount):
        self.balance = self.balance + ammount
    
    def setBalance(self,amount):
        self.balance = amount
    
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
    




# if __name__ == '__main__':
#     # testing player class
#     
#     testdeck = deck()
#     
#     testdeck.shuffe()
#     
#     testplayer = player("sunny",100)
#     
#     print(testplayer)
#     
#     playerbet = testplayer.placeBet()
#     
#     print(f'{testplayer.getName()} has placed a bet of {playerbet}')
#     
#     print(f'dealing card to {testplayer.getName()}')
#     testplayer.hit(testdeck)
#     testplayer.hit(testdeck)
#     
#     print(f"{testplayer.getName()} has the folloiwng hand {testplayer.getHand()}")
#     
