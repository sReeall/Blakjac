'''
Created on 14 Jul 2018

@author: sande
'''
import unittest
import Deck

class Test(unittest.TestCase):

    # Test class card
    def testCardNumRank(self):
        card = Deck.card('heart',2)

        self.assertTrue(card.rank == 2)
        self.assertTrue(card.suit == 'heart')
        self.assertTrue(card.value == (2))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDeck']
    unittest.main()