# TODO - refactor this code

def _isStraight(rank_list):
    ''' 
    sorts the rank list in order
    recreates a list from the smallest rank and largest rank
    if these are equal then it is consecutive
    inspiration: https://www.geeksforgeeks.org/python-check-if-list-contains-consecutive-numbers/
    '''
    smallest_rank = min(rank_list)
    largest_rank = max(rank_list)
    recreate_rank_list = list(range(smallest_rank, largest_rank + 1))

    # special case for wheel, 'A2345'
    STRAIGHT_WHEEL = [2,3,4,5,14]

    return sorted(rank_list) == recreate_rank_list or sorted(rank_list) == STRAIGHT_WHEEL

def winninghand(players):
    '''
    Takes an array of players hands and finds the best hand
    Eventually return the player's hand that won (by finding the player number)
    '''
    result = None
    for hand in enumerate(players,1):
        # label the players with numbers
        player_no, cards = hand
        
        #print(player_no)
        #print(cards)
        
        # unzip the cards array for easier checking of grouping
        
#         groups = [[suit for rank,suit in cards],
#                   [rank for rank,suit in cards]]
        
        suits = [suit for rank,suit in cards]
        ranks = [rank for rank,suit in cards]
#         print(f'suits: {suits}')
#         print(f'ranks: {ranks}')
        
      
        # need to get the counts of each element
        # compare the counts of the highest groups
        # finding "pairs" algorithm
        rank_counts = {}
        for rank in ranks:
            if ranks.count(rank) > 1:
                rank_counts[rank] = ranks.count(rank)
#         print(rank_counts)
        
        # only one "pair" type is in the dict
        if len(rank_counts.keys()) == 1:
            #print(rank_counts.values())
            if 3 in rank_counts.values():
                result = 'trips'
            elif 4 in rank_counts.values():
                result = 'quads'
            elif 2 in rank_counts.values():
                result = 'pair'
        elif len(rank_counts.keys()) == 2:
            # checking if pair dict values contain a 2 and 3 
            # in other words, need 3 of a kind AND a pair
            # https://stackoverflow.com/a/6159329/4376173
            FULL_HOUSE_PAIR_COMBO = [2,3]
            if all(pair_count in list(rank_counts.values()) for pair_count in FULL_HOUSE_PAIR_COMBO):
                result = 'full house'
            elif 2 in set(rank_counts.values()):
                result = 'two pair'
            else:
                raise Exception('calculation error for full house or two pair')
        else:
            if len(set(suits)) == 1:
                if _isStraight(ranks):
                    result = 'straight flush'
                else:
                    result = 'flush'
            else:
                if _isStraight(ranks):
                    result = 'straight'
                else:
                    result = 'nothing'
    return result