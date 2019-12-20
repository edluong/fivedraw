from hand import Hand
from card import Card
import unittest

class TestHand(unittest.TestCase):
    
    def setUp(self):

        self.hand = Hand()
        self.card = Card(1,'spade')
        self.hand.add_card(self.card)
   
    def test_add_card(self):
        self.assertTrue(self.card in self.hand.get_hand())

    def test_hand_size(self):
        self.assertEqual(1,self.hand.hand_size())

    def test_reset_hand(self):
        self.hand.reset_hand()
        self.assertEqual([],self.hand.get_hand())
