from constants import RANK_NAME

class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self,card):
        self.hand.append(card)

    def hand_size(self):
        return len(self.hand)
    
    def print_hand(self):
        '''
            prints hand from smallest to largest rank
            also with the index of the card
        '''
        if self.hand_size() < 1:
            print('No Cards')
        for card in enumerate(sorted(self.hand), 1):
            _index, _card_tuple = card
            rank, suit = _card_tuple
            
            rank_name = RANK_NAME.get(rank) or rank
            card_output = (rank_name, suit)
            print(f'{_index}: {card_output}')

    def reset_hand(self):
        self.hand.clear()
    
    def get_hand(self):
        return self.hand
    
    def discard(self, indexes):
        '''
            given a list of indexes, removes the index of the card selected
        '''
        if len(indexes) == 5:
            self.reset_hand()
        
        _list_to_remove = []
        for index in indexes:
            for card in enumerate(sorted(self.get_hand()), 1):
                _index, _card_tuple = card
                if _index == index:
                    _list_to_remove.append(_card_tuple)
        for _card in _list_to_remove:
            self.hand.remove(_card)
    
    def set_hand(self, hand):
        '''
            settter method

            Parameter: 
            argument1 (array):  array comprises of tuples of "cards"
        '''
        self.hand = hand
                