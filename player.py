from hand import Hand

class CantOverBetError(Exception):
    '''amount bet was higher than stack size! '''

class Player:
    
    def __init__(self, stack, isDealer = False):
        self.hand = Hand()
        self.stack = stack
        self.isDealer = isDealer
    
    # TODO - set up a unit test
    def bet(self, amount):
        if amount > self.stack:
            raise CantOverBetError
        self.stack-= amount
        return amount
    
    def dealer_status(self):
        return self.isDealer
    
    def stack_size(self):
        return self.stack
    
    def get_hand(self):
        return self.hand
    
    def winpot(self, amount):
        self.stack += amount
