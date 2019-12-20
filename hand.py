class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self,card):
        self.hand.append(card)

    def hand_size(self):
        return len(self.hand)
    
    def print_hand(self):
        for card in self.hand:
            print(card)
    
    def reset_hand(self):
        self.hand.clear()
    
    def get_hand(self):
        return self.hand
