class Card():

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        
        lookup = {1:'ace',11:'jack',12:'queen',13:'king'}
        
        if lookup.get(self.rank):
            return "({},{})".format(lookup.get(self.rank),self.suit)
        else:
            return "({},{})".format(self.rank,self.suit)
            
