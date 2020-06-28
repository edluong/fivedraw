from hand import Hand
from card import Card
import unittest

class TestHand(unittest.TestCase):
    
    def setUp(self):

        self.hand = Hand()
        self.card = (14,'Spades')
        self.hand.add_card(self.card)
   
    def test_add_card(self):
        self.assertTrue(self.card in self.hand.hand)

    def test_hand_size(self):
        self.assertEqual(1,self.hand.hand_size())

    def test_reset_hand(self):
        self.hand.reset_hand()
        self.assertEqual([], self.hand.hand)

    def test_discard_hand(self):
        self.hand.discard([1]) # enumerate starts at 1 not traditional 0
        self.assertEqual([], self.hand.hand)
        