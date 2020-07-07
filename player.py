from constants import RANK_NAME

class CantOverBetError(Exception):
    '''amount bet was higher than stack size! '''

class Player:
    
    def __init__(self, stack, isDealer = False):
        self.hand = []
        self.stack = stack
        self.isDealer = isDealer
    
    def __eq__(self, other):
        return self.hand == other.hand

    def bet(self, amount):
        if amount > self.stack:
            raise CantOverBetError
        self.stack-= amount
        return amount
    
    def dealer_status(self):
        return self.isDealer
    
    def stack_size(self):
        return self.stack
    
    def set_hand(self, hand):
        self.hand = hand
    
    def winpot(self, amount):
        self.stack += amount
    
    def print_hand(self):
        '''
            prints hand from smallest to largest rank
            also with the index of the card
        '''
        if len(self.hand) < 1:
            print('No Cards')
        for card in enumerate(sorted(self.hand), 1):
            _index, _card_tuple = card
            rank, suit = _card_tuple
            
            rank_name = RANK_NAME.get(rank) or rank
            card_output = (rank_name, suit)
            print(f'{_index}: {card_output}')

    def discard(self, indexes):
        '''
            given a list of indexes, removes the index of the card selected
        '''
        if len(indexes) == 5:
            self.hand.clear()
        
        _list_to_remove = []
        for index in indexes:
            for card in enumerate(sorted(self.hand), 1):
                _index, _card_tuple = card
                if _index == index:
                    _list_to_remove.append(_card_tuple)
        for _card in _list_to_remove:
            self.hand.remove(_card)
