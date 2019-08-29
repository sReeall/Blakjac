# Blakjac

This is a simple implementation of the famous casino game Black Jack.
The game is command line based, with awesome ASCII graphics :)

To start the game, take a copy of the project and run the game.py file, enjoy!

Comments welcome 

## Coding Notes:

1. Could have used dictionary/ hash table to look up numeric value of card rank.

In my code, I created a try and except as follows:

        # values assigned automatically based on rank
        try: # add cast to int
            self.value = int(rank),
        except: # must not be 2 - 10 rank
            # check if ace
            if rank != 'A' : self.value = 10,
            else: self.value = 11,1
			
