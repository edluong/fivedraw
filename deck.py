from card import Card

class Deck:

    suit = ['heart','club','spade','diamond']

    def __init__(self):

#        # fill up the deck
#        deck = []
#
#        for rank in range(1,14):
#            for suit in self.suit:
#                self.deck.append(Card(rank,suit))
#        
        self.deck = [Card(rank,suit) for rank in range(1,14) for suit in self.suit]

    
    def print_deck(self):
        for card in self.deck:
            print(card,end="\n")
