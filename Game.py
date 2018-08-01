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
        
        sleep(3)
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
        
        if player1.hand.isBust:
            
            if dealer1.hand.isBust:
                #both player and dealer are bust
                
                print(f'{player1.getName()} and {dealer1.getName()} are bust!')
                print(f'Game is a a draw, returning bet')
                
                sleep(3)
                
                player1.setBalance(player1.getBalance() + player1.getBet())
                
                print('')
                print(f'Player: {player1.getName()}')
                print(f'Current Balance: {player1.getBalance()}')
            
                sleep(3)
            
            else: 
                #deal is not bust, player must have lost
                
                print(f'{player1.getName()} lost!')
                #no futher processing as replay logic is clear bet and preserve player balancee.
                
                sleep(3)
            
        else: #player hand is not bust
            
            if dealer1.hand.isBust:
                # player is not bust, dealer is bust, player wins!
                # double bet and add to balance 
                print(f'{player1.getName()} is a winner!')
                
                sleep(3)
                
                player1.setBalance(player1.getBalance() + (player1.getBet() * 2) )
                
                print('')
                print(f'Player: {player1.getName()}')
                print(f'Current Balance: {player1.getBalance()}')
            
                sleep(3)
            
            else:
                #player is not bust and dealer is not bust
                #print('neither player or dealer is bust!')
            
                # add logic to handle winning hand
                
                if player1.hand.getvalue() > dealer1.hand.getvalue():
                    #player wins
                    print(f'{player1.getName()} is the winner')
                    player1.setBalance(player1.getBalance() + (player1.getBet() * 2) )
                
                    print('')
                    print(f'Player: {player1.getName()}')
                    print(f'Current Balance: {player1.getBalance()}')                    
            
                    sleep(3)
                elif player1.hand.getvalue() < dealer.hand.getvalue():
                    #dealer wins
                    print(f'{dealer1.getName()} is the winner')
                else:
                    #must be a draw
                    print(f'Game is a a draw, returning bet')
                
                    sleep(3)
                
                    player1.setBalance(player1.getBalance() + player1.getBet())
                    
                    print('')
                    print(f'Player: {player1.getName()}')
                    print(f'Current Balance: {player1.getBalance()}')
                
                    sleep(3)
        
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