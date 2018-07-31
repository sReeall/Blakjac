'''
Created on 29 Jul 2018

@author: sReeall
'''
from Player import player
from Dealer import dealer
from Table import table
from Deck import deck
from time import sleep

def startGame():
        
    print('Welcome to BlakJac')
    
    print('')
    
    # setup deck
    
    gamedeck = deck()
    
    gamedeck.shuffe()
    
    # Setup player and dealer
    
    
    
    player1name = input('Please enter your name: ')
    
    player1 = player(player1name)
    
    dealer1 = dealer()
    
    gametable = table(player1,dealer1)
    
    while True:
        try:
            deposit = int(input('How much would you like to deposit?:'))
            break
        except:
            print('Oops! deposit needs to be a number. Please try again')
    
    player1.setBalance(deposit)
    
    print(f'Welcome {player1.getName()} your balance is now {player1.getBalance()}')
    
    while True:
        startgame = str(input('Are you to start?[y/n]'))
        if startgame.lower() == 'y': break
        elif startgame.lower() == 'n': 
            print('Ok we will wait!')
        else: print('Oops! You need to enter y or n')
    
    print('Get Ready...')
    sleep(3)
    
    # main game logic
    
    while True:
        gametable.displayBoard()
        
        player1.placeBet()
        
        print('')
        print('')
        
        gametable.displayBoard()
        
        print('Dealing cards')
        
        sleep(2)
        
        player1.hit(gamedeck)
        
        gametable.displayBoard()
        
        sleep(2)
        
        player1.hit(gamedeck)
    
        gametable.displayBoard()
        
       
        sleep(2)
        
        dealer1.hit(gamedeck)
    
        gametable.displayBoard()
        
        sleep(2)
    
        dealer1.hit(gamedeck)
        
        gametable.displayBoard()
        
        sleep(2)
        
        # choose hit or stick logic
        
        while True:
    
            #need to check if player already has black jack
            
            if player1.hand.isblackjack: 
                print(f'{player1.getName()} has blackJack!')
                break
            
            hit = input(f'{player1.getName()} hit or stick? [enter h or s]:')
            if hit.lower() == 'h':
                #hit
                player1.hit(gamedeck)
                
                gametable.displayBoard()
        
                sleep(2)
                            
                # check for black jack
                if player1.hand.isblackjack:
                    print(f'{player1.getName()} has blackJack!')
                    break
                #check for bust
                elif player1.hand.isBust:
                    print(f'{player1.getName()} is Bust!')
                    break
                # ask for hit or stick again
                else:
                    continue
                
            elif hit.lower() == 's':
                #stick
                print('Stick')
                break
            else:
                #incorrect input
                print("Incorrect option, please use h or s for hit or stick")
        
        # dealer1 turn logic
        
        print('Dealers Turn')
        
        sleep(2)
        
        # show dealers hidden card
        dealer1.setIsTurn(True)
        
        gametable.displayBoard()
        
        while True:
            
            # check to see if dealer has black jack
            
            if dealer1.hand.isblackjack: 
                print(f'{dealer1.getName()} has blackJack')
                break
    
            
            if dealer1.hand.isBust:
                print(f'{dealer1.getName()} is Bust!')
                break
            
            
            # check if dealer has less then 17, or 17 but with an ace, they hit
            
            if (dealer1.hand.getvalue() < 17) or (dealer1.hand.getvalue() == 17 and dealer1.hand.containsAce):
                print(f'{dealer1.getName()} takes a HIT!')
                dealer1.hit(gamedeck)
                
                gametable.displayBoard()
    
                sleep(2)
                
                continue
            else:
                print(f'{dealer1.getName()} STICKS!')
                break
            
        # bet win/ loss logic
        
        # if player bust, check to see if dealer bust = draw
        # else, if deal hans't bust = loose bet
        
        
        
        # player hand beats
        
        # replay logic
        
        while True:
            
            playagain = input('Play again?[y or n]').lower()
                     
            if (playagain == 'y'): 
                isGameOn = True
                break
            elif (playagain == 'n'): 
                isGameOn = False
                break
            else:
                print('Opps! please enter y or n') 
                continue
            
        if isGameOn: 
            # need to clear board, and reset player hanad and reset dealer hand
            player1.clearBet()
            player1.hand.clearHand()
            
            dealer1.hand.clearHand()
            dealer1.setIsTurn(False)
            
            #add condition to test if deck is 50% empty (len <= 26), start a new deck and shuffle
            
            continue
        else:
            print('GoodBye!') 
            break

if __name__=='__main__':
    
    startGame()    