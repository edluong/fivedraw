class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self,card):
        self.hand.append(card)

    def hand_size(self):
        return len(hand)
    
    def print_hand(self):
        for card in self.hand:
            print(card)

