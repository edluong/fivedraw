import unittest

import constants as con
from player import Player
import pokerengine as pe # TODO - use from and import the methods
import tests.test_hand_constants as hc # added tests. since Makefile is above

class TestHandRankings(unittest.TestCase):
    def setUp(self):
        self.hands = hc.hands
    
    def test_high_card(self):
        rank_desc = 'high card'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('high_card'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

    def test_pair(self):
        rank_desc = 'pair'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('pair'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))
    
    def test_two_pair(self):
        rank_desc = 'two pair'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('two_pair'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

    def test_trips(self):
        rank_desc = 'trips'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('trips'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

    def test_straight(self):
        rank_desc = 'straight'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('straight'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

    # A2345
    def test_straight_wheel(self):
        rank_desc = 'straight'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('straight_wheel'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

    # 10JQKA
    def test_straight_broadway(self):
        rank_desc = 'straight'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('straight_broadway'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

    def test_flush(self):
        rank_desc = 'flush'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('flush'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

    def test_full_house(self):
        rank_desc = 'full house'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('full_house'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))
    
    def test_quads(self):
        rank_desc = 'quads'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('quads'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

    def test_straight_flush(self):
        rank_desc = 'straight flush'
        r_rank_name, r_ranking_num = pe.hand_rank(self.hands.get('straight_flush'))
        #tests
        self.assertEqual(r_rank_name, rank_desc)
        self.assertEqual(r_ranking_num, con.RANKING.get(rank_desc))

class TestWinningHand(unittest.TestCase):

    def setUp(self):
        # get a dict of player objs
        # static information
        STARTING_STACK_SIZE = 100
        self.players = hc.make_player_dict(hc.hands, STARTING_STACK_SIZE)
        
    def test_pair_vs_trips(self):
        # add to players array
        _players = [self.players.get('pair'), self.players.get('trips')]

        # winning description and results of winninghand
        _winning_desc = 'trips'
        r_player, r_winning_desc = pe.winninghand(_players)

        # tests
        self.assertEqual(r_player, self.players.get('trips'))
        self.assertEqual(r_winning_desc, _winning_desc)
    
    def test_multiple_players(self):
        # add players to players array
        _players = []

        _players.append(self.players.get('pair'))
        _players.append(self.players.get('two_pair'))
        _players.append(self.players.get('trips'))
        _players.append(self.players.get('full_house'))

        # add players to players_diff_order array
        _players_diff_order = []
        _players_diff_order.append(self.players.get('full_house'))
        _players_diff_order.append(self.players.get('trips'))
        _players_diff_order.append(self.players.get('two_pair'))
        _players_diff_order.append(self.players.get('pair'))

        # winning description and results of winninghand
        _winning_desc = 'full house'
        r_player, r_winning_desc = pe.winninghand(_players)
        r_do_player, r_do_winning_desc = pe.winninghand(_players_diff_order)

        # tests
        self.assertEqual(r_player, self.players.get('full_house'))
        self.assertEqual(r_winning_desc, _winning_desc)
        self.assertEqual(r_do_player, self.players.get('full_house'))
        self.assertEqual(r_do_winning_desc, _winning_desc)

    def test_same_ranking_high_card(self):
        # load two types of ordering of player arrays
        _players = [self.players.get('high_card'), self.players.get('high_card_ace')] 
        _players_diff_order = [self.players.get('high_card_ace'), self.players.get('high_card')] 

        # results
        _winning_desc = 'high card'
        r_player, r_winning_desc = pe.winninghand(_players)
        r_do_player, r_do_winning_desc = pe.winninghand(_players_diff_order)

        # tests
        self.assertEqual(r_player, self.players.get('high_card_ace'))
        self.assertEqual(r_winning_desc, _winning_desc)
        self.assertEqual(r_do_player, self.players.get('high_card_ace'))
        self.assertEqual(r_do_winning_desc, _winning_desc)
    
    def test_same_ranking_flush(self):
        # load two types of ordering of player arrays
        _players = [self.players.get('flush_same_rank'), self.players.get('flush_same_rank_win')] 
        _players_diff_order = [self.players.get('flush_same_rank_win'), self.players.get('flush_same_rank')] 

        # results
        _winning_desc = 'flush'
        r_player, r_winning_desc = pe.winninghand(_players)
        r_do_player, r_do_winning_desc = pe.winninghand(_players_diff_order)

        # tests
        self.assertEqual(r_player, self.players.get('flush_same_rank_win'))
        self.assertEqual(r_winning_desc, _winning_desc)
        self.assertEqual(r_do_player, self.players.get('flush_same_rank_win'))
        self.assertEqual(r_do_winning_desc, _winning_desc)
    
    def test_same_ranking_fullhouse(self):
        _players = [self.players.get('full_house'), self.players.get('full_house_aces')] 
        _players_diff_order = [self.players.get('full_house_aces'), self.players.get('full_house')] 

        # results
        _winning_desc = 'full house'
        r_player, r_winning_desc = pe.winninghand(_players)
        r_do_player, r_do_winning_desc = pe.winninghand(_players_diff_order)

        # tests
        self.assertEqual(r_player, self.players.get('full_house_aces'))
        self.assertEqual(r_winning_desc, _winning_desc)
        self.assertEqual(r_do_player, self.players.get('full_house_aces'))
        self.assertEqual(r_do_winning_desc, _winning_desc)
    
    # example: 22XXX vs 22XXX
    def test_tied_pair(self):
        _players = [self.players.get('tied_hand_pair'), self.players.get('tied_hand_pair_two')]

        _winning_desc = 'pair'
        r_players, r_winning_desc = pe.winninghand(_players)

        self.assertEqual(_players, r_players)
        self.assertEqual(_winning_desc, r_winning_desc)
    
    # example: AKQJ9 AKQJ9
    def test_tied_high_card(self):
        _players = [self.players.get('tied_hand_high_card'), self.players.get('tied_hand_high_card_two')]

        _winning_desc = 'high card'
        r_players, r_winning_desc = pe.winninghand(_players)

        self.assertEqual(_players, r_players)
        self.assertEqual(_winning_desc, r_winning_desc)
    
    # example: AAKKQ vs AAKKQ
    def test_tied_two_pair(self):
        _players = [self.players.get('tied_hand_two_pair'), self.players.get('tied_hand_two_pair_two')]

        _winning_desc = 'two pair'
        r_players, r_winning_desc = pe.winninghand(_players)

        self.assertEqual(_players, r_players)
        self.assertEqual(_winning_desc, r_winning_desc)

    # example: AKQJ10 vs AKQJ10
    def test_tied_straight(self):
        _players = [self.players.get('tied_hand_straight'), self.players.get('tied_hand_straight')]

        _winning_desc = 'straight'
        r_players, r_winning_desc = pe.winninghand(_players)

        self.assertEqual(_players, r_players)
        self.assertEqual(_winning_desc, r_winning_desc)

if __name__ == '__main___':
    unittest.main()
