# used for testing
from player import Player

# test dict of hardcoded hand cases
hands = {
    # "pair" hands
    'pair': [(2,'Spades'),(2,'Diamonds'),(3,'Clubs'),(4,'Hearts'),(5,'Diamonds')],
    'pair_tied' : [(2,'Clubs'),(2,'Hearts'),(3,'Spades'),(4,'Diamonds'),(5,'Hearts')],
    'two_pair' : [(2,'Spades'),(2,'Diamonds'),(3,'Clubs'),(3,'Hearts'),(4,'Diamonds')],
    'trips' : [(2,'Spades'),(2,'Diamonds'),(2,'Clubs'),(3,'Hearts'),(4,'Diamonds')],
    'full_house' : [(3,'Spades'),(3,'Hearts'),(3,'Clubs'),(2,'Spades'),(2,'Clubs')],
    'quads' : [(2,'Spades'),(2,'Diamonds'),(2,'Clubs'),(2,'Hearts'),(8,'Diamonds')],
    'full_house_aces' : [(14,'Spades'),(14,'Hearts'),(14,'Clubs'),(2,'Hearts'),(2,'Diamonds')],

    # straight/flush algorithm
    'straight' : [(2,'Spades'),(3,'Diamonds'),(4,'Clubs'),(5,'Hearts'),(6,'Diamonds')],
    'straight_wheel' : [(14,'Spades'),(2,'Diamonds'),(3,'Clubs'),(4,'Hearts'),(5,'Diamonds')],
    'straight_broadway' : [(10,'Spades'),(11,'Diamonds'),(12,'Clubs'),(13,'Hearts'),(14,'Diamonds')],
    'flush' : [(2,'Spades'),(3,'Spades'),(4,'Spades'),(5,'Spades'),(7,'Spades')],
    'straight_flush' : [(2,'Spades'),(3,'Spades'),(4,'Spades'),(5,'Spades'),(6,'Spades')],
    'flush_same_rank_win' : [(6,'Spades'),(11,'Spades'),(12,'Spades'),(13,'Spades'),(14,'Spades')],
    'flush_same_rank' : [(5,'Spades'),(11,'Spades'),(12,'Spades'),(13,'Spades'),(14,'Spades')],

    # high card
    'high_card' : [(2,'Spades'),(3,'Diamonds'),(4,'Clubs'),(5,'Hearts'),(7,'Diamonds')],
    'high_card_ace' : [(2,'Spades'),(3,'Diamonds'),(4,'Clubs'),(6,'Hearts'),(14,'Diamonds')],

    # test_tied_pair
    'tied_hand_pair' : [(2,'Spades'),(2,'Diamonds'),(4,'Clubs'),(5,'Hearts'),(7,'Diamonds')],
    'tied_hand_pair_two' : [(2,'Clubs'),(2,'Hearts'),(4,'Spades'),(5,'Clubs'),(7,'Hearts')], 

    # test_tied_high_card
    'tied_hand_high_card' : [(14,'Spades'),(13,'Spades'),(12,'Spades'),(11,'Spades'),(9,'Diamonds')],
    'tied_hand_high_card_two' : [(14,'Diamonds'),(13,'Diamonds'),(12,'Diamonds'),(11,'Diamonds'),(9,'Spades')],

    # test_tied_two_pair
    'tied_hand_two_pair' : [(14,'Spades'),(14,'Diamonds'),(13,'Diamonds'),(13,'Hearts'),(12,'Diamonds')],
    'tied_hand_two_pair_two' : [(14,'Clubs'),(14,'Hearts'),(13,'Spades'),(13,'Clubs'),(12,'Hearts')],

    # test_tied_straight
    'tied_hand_straight' : [(14,'Spades'),(13,'Diamonds'),(12,'Diamonds'),(11,'Hearts'),(10,'Diamonds')],
    'tied_hand_straight_two' : [(14,'Clubs'),(13,'Hearts'),(12,'Spades'),(11,'Clubs'),(10,'Hearts')],  
}

# loading up the players dict
def make_player_dict(hands, stack_size):
    '''
        Util function to transform a list of hardcoded hands and adds them to players
        
        Parameter:
        argument1 (dict): key - ranking of hand ,value - list of tuples of "cards"
        argument2 (int): starting stack size
        
        Returns:
        (dict): key - ranking name, value - Player obj with the associated ranking hand
    '''
    players = {}
    for name, cards in hands.items():
        player = Player(stack_size)
        hand = []
        player.hand = cards
        players.update({name: player})
    return players
