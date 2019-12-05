from hand import Hand
from card import Card

test_hand = Hand()
test_card = Card(1,'spade')

test_hand.add_card(test_card)

test_hand.print_hand()

test_hand.reset_hand()

print('Hand Size: {}'.format(test_hand.hand_size()))
test_hand.print_hand()

