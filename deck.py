from card import Card
from random import shuffle

class Deck:

    suit = ['heart','club','spade','diamond']

    def __init__(self):
        self.deck = [Card(rank,suit) for rank in range(1,14) for suit in self.suit]

    def load_deck(self):
        return [Card(rank,suit) for rank in range(1,14) for suit in self.suit]
 
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
