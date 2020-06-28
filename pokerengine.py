# TODO - winninghand needs to account for four tied hands

from constants import STRAIGHT_WHEEL, RANKING

def _isStraight(rank_list):
    ''' 
    sorts the rank list in order
    recreates a list from the smallest rank and largest rank
    if these are equal then it is consecutive
    inspiration: https://www.geeksforgeeks.org/python-check-if-list-contains-consecutive-numbers/
    '''
    if len(rank_list) < 5:
        raise Exception(f"hand length is now {len(rank_list)}!")

    smallest_rank = min(rank_list)
    largest_rank = max(rank_list)
    recreate_rank_list = list(range(smallest_rank, largest_rank + 1))

    return sorted(rank_list) == recreate_rank_list or sorted(rank_list) == STRAIGHT_WHEEL

def _straight_and_or_flush(rank_list, suit_list):
    result = None

    # checking if all the suit values are the same
    if len(set(suit_list)) == 1:
        result = 'straight flush' if _isStraight(rank_list) else 'flush'
    else:
        result = 'straight' if _isStraight(rank_list) else 'high card'
    return result

def _same_rank_winning_hand(playerone, playertwo):

    handone = playerone.hand.hand
    handtwo = playertwo.hand.hand

    # find the different cards from the both hands
    diff_one = set(handone).difference(set(handtwo))
    diff_two = set(handtwo).difference(set(handone))

    ranks_handone = [rank for rank, suit in handone]
    ranks_handtwo = [rank for rank, suit in handtwo]

    if sorted(ranks_handone) == sorted(ranks_handtwo):
        return [playerone, playertwo] # return both hands
    elif max(diff_one) > max(diff_two):
        return playerone
    else:
        return playertwo

def hand_rank(hand):
    '''
    evaluates a hand of five cards

    Returns:
    tuple: (rank name, rank number)
    '''
    result = None
    suits = [suit for rank,suit in hand]
    ranks = [rank for rank,suit in hand]
    
    # need to get the counts of each element
    # compare the counts of the highest groups
    # finding "pairs" algorithm
    rank_counts = {}
    for rank in ranks:
        if ranks.count(rank) > 1:
            rank_counts[rank] = ranks.count(rank)
    
    # pair count with the corresponding ranking strength 
    # larger the better
    _pair_results = {
        2: 'pair',
        3: 'trips',
        4: 'quads'
    }

    # only one "pair" type is in the dict
    if len(rank_counts) == 1:
        # taking the max because there is only one value
        result = _pair_results[max(rank_counts.values())]
    # two different types of "pairs"
    elif len(rank_counts) == 2:
        # checking if pair dict values contain a 2 and 3 
        # in other words, need 3 of a kind AND a pair
        # https://stackoverflow.com/a/6159329/4376173
        
        _FULL_HOUSE_PAIR_COMBO = [2,3]

        if all(pair_count in list(rank_counts.values()) for pair_count in _FULL_HOUSE_PAIR_COMBO):
            result = 'full house'
        elif 2 in set(rank_counts.values()):
            result = 'two pair'
        else:
            raise Exception('calculation error for full house or two pair')
    else:
        result = _straight_and_or_flush(ranks, suits)
    return (result, RANKING[result])


def winninghand(players):
    '''
    Takes an array of Player objects and finds the best hand

    Parameters:
    argument1 (array): this will be an array of hand objects

    Returns:
    tuple: (winning hand(s), hand rank desc)

    ([(10,'D'),(J,'D')(Q,'D')(K,'D')(A,'D')], 'straight flush')
    '''
    _max_rank_strength = 0
    _max_player = None
    _max_desc = None
    
    for player in players:

        # get a ranking for the hand
        handrank_tuple = hand_rank(player.hand.hand)
        
        # separate out the results
        desc, rank_strength = handrank_tuple
        
        # determine if this ranking is higher than what we've seen so far
        # if its higher replace it as the highest ranking
        # if its the same ranking, compare the actual cards
        if rank_strength > _max_rank_strength:
            _max_rank_strength = rank_strength
            _max_player = player
            _max_desc = desc
        elif rank_strength == _max_rank_strength:
            _max_player = _same_rank_winning_hand(_max_player, player)
    return (_max_player, _max_desc)