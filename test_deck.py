from deck import Deck

# print the deck
d = Deck()
d.print_deck()

# shuffle the deck
d.shuffle()
print('shuffling the deck...')

# show draw is working
print(d.draw())
print(d.draw())
