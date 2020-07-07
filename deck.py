from random import shuffle
from constants import SUIT

class Deck:

    suit = SUIT

    def load_deck(self):
        return [(rank,suit) for rank in range(2,15) for suit in self.suit]
    
    def __init__(self):
        self.deck = self.load_deck()

    def print_deck(self):
        for card in self.deck:
            print(card,end="\n")
    
    def draw(self):
        return self.deck.pop(0)
    
    def shuffle(self):
        shuffle(self.deck)
    
    def reload(self):
        self.deck.clear()
        self.deck = self.load_deck()
        self.shuffle()
    
    def deck_size(self):
        return len(self.deck)
