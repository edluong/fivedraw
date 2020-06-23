import constants as con 

class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self,card):
        self.hand.append(card)

    def hand_size(self):
        return len(self.hand)
    
    def print_hand(self):
        for card in sorted(self.hand):
            rank, suit = card
            
            rank_name = con.RANK_NAME.get(rank) or rank
            card_output = (rank_name, suit)
            print(card_output)

    def reset_hand(self):
        self.hand.clear()
    
    def get_hand(self):
        return self.hand
    
    def discard(self, card):
        pass
