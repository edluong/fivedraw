from deck import Deck
import unittest


class TestDeck(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()
    
    def test_decksize(self):
        self.assertEqual(52,self.deck.deck_size())
    
    def test_draw(self):
        self.deck.draw()
        self.assertEqual(51,self.deck.deck_size())

    def test_reload(self):
        self.deck.reload()
        self.assertEqual(52,self.deck.deck_size())
