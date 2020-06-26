import unittest

import constants as con
from player import Player
import pokerengine as pe # TODO - use from and import the methods
import tests.test_hand_constants as hc # added tests. since Makefile is above

class TestHandRankings(unittest.TestCase):
    
    def test_high_card(self):
        rank_desc = 'high card'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.high_card), result)

    def test_pair(self):
        rank_desc = 'pair'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.pair), result)
    
    def test_two_pair(self):
        rank_desc = 'two pair'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.two_pair), result)

    def test_trips(self):
        rank_desc = 'trips'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.trips), result)

    def test_straight(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.straight), result)

    # A2345
    def test_straight_wheel(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.straight_wheel), result)

    # 10JQKA
    def test_straight_broadway(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.straight_broadway), result)

    def test_flush(self):
        rank_desc = 'flush'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.flush), result)

    def test_full_house(self):
        rank_desc = 'full house'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.full_house), result)
    
    def test_quads(self):
        rank_desc = 'quads'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.quads), result)

    def test_straight_flush(self):
        rank_desc = 'straight flush'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe.hand_rank(hc.straight_flush), result)

class TestWinningHand(unittest.TestCase):

    def setUp(self):
        _stack_size = 100
        self.players = []
        self.players_diff_order = []

        # initialize the players
        self.p_pair = Player(_stack_size)
        self.p_two_pair = Player(_stack_size)
        self.p_trips = Player(_stack_size)
        self.p_full_house = Player(_stack_size)

        # set hands to players
        self.p_pair.set_hand(hc.pair)
        self.p_two_pair.set_hand(hc.two_pair)
        self.p_trips.set_hand(hc.trips)
        self.p_full_house.set_hand(hc.full_house)

        
    def test_pair_vs_trips(self):
        # add to players array
        self.players.append(self.p_pair)
        self.players.append(self.p_trips)

        # winning description and results of winninghand
        _winning_desc = 'trips'
        r_player, r_winning_desc = pe.winninghand(self.players)

        self.assertEqual(r_player, self.p_trips)
        self.assertEqual(r_winning_desc, _winning_desc)
    
    def test_multiple_players(self):
        # add players to players array
        self.players.append(self.p_pair)
        self.players.append(self.p_two_pair)
        self.players.append(self.p_trips)
        self.players.append(self.p_full_house)

        # add players to players_diff_order array
        self.players_diff_order.append(self.p_full_house)
        self.players_diff_order.append(self.p_trips)
        self.players_diff_order.append(self.p_two_pair)
        self.players_diff_order.append(self.p_pair)

        # winning description and results of winninghand
        _winning_desc = 'full house'
        r_player, r_winning_desc = pe.winninghand(self.players)
        r_do_player, r_do_winning_desc = pe.winninghand(self.players_diff_order)

        # tests
        self.assertEqual(r_player, self.p_full_house)
        self.assertEqual(r_winning_desc, _winning_desc)
        self.assertEqual(r_do_player, self.p_full_house)
        self.assertEqual(r_do_winning_desc, _winning_desc)


    def test_same_ranking_high_card(self):
        players = [] 
        players.append(hc.high_card)
        players.append(hc.high_card_ace)

        # test different order
        players_diff_order = []
        players_diff_order.append(hc.high_card_ace)
        players_diff_order.append(hc.high_card)

        _winning_desc = 'high card'
        result = (hc.high_card_ace, _winning_desc)

        self.assertEqual(pe.winninghand(players), result)
        self.assertEqual(pe.winninghand(players_diff_order), result)
    
    def test_same_ranking_flush(self):
        players = []
        players.append(hc.flush_same_rank)
        players.append(hc.flush_same_rank_win)

        players_diff_order = []
        players_diff_order.append(hc.flush_same_rank_win)
        players_diff_order.append(hc.flush_same_rank)
        
        _winning_desc = 'flush'
        result = (hc.flush_same_rank_win, _winning_desc)
        self.assertEqual(pe.winninghand(players), result)
        self.assertEqual(pe.winninghand(players_diff_order), result)
    
    def test_same_ranking_fullhouse(self):
        players = []
        players.append(hc.full_house)
        players.append(hc.full_house_aces)

        players_diff_order = []
        players_diff_order.append(hc.full_house_aces)
        players_diff_order.append(hc.full_house)

        _winning_desc = 'full house'
        result = (hc.full_house_aces, _winning_desc)
        self.assertEqual(pe.winninghand(players), result)
        self.assertEqual(pe.winninghand(players_diff_order), result)
    
    # example: 22XXX vs 22XXX
    def test_tied_pair(self):
        players = []
        players.append(hc.tied_hand_pair)
        players.append(hc.tied_hand_pair_two)

        _winning_desc = 'pair'
        result = ([hc.tied_hand_pair, hc.tied_hand_pair_two], _winning_desc)
        self.assertEqual(pe.winninghand(players), result)
    
    # example: AKQJ9 AKQJ9
    def test_tied_high_card(self):
        players = []
        players.append(hc.tied_hand_high_card)
        players.append(hc.tied_hand_high_card_two)

        _winning_desc = 'high card'
        result = ([hc.tied_hand_high_card, hc.tied_hand_high_card_two], _winning_desc)
        self.assertEqual(pe.winninghand(players), result)
    
    # example: AAKKQ vs AAKKQ
    def test_tied_two_pair(self):
        players = []
        players.append(hc.tied_hand_two_pair)
        players.append(hc.tied_hand_two_pair_two)

        _winning_desc = 'two pair'
        result = ([hc.tied_hand_two_pair, hc.tied_hand_two_pair_two], _winning_desc)
        self.assertEqual(pe.winninghand(players), result)

    # example: AKQJ10 vs AKQJ10
    def test_tied_straight(self):
        players = []
        players.append(hc.tied_hand_straight)
        players.append(hc.tied_hand_straight_two)

        _winning_desc = 'straight'
        result = ([hc.tied_hand_straight, hc.tied_hand_straight_two], _winning_desc)
        self.assertEqual(pe.winninghand(players), result)
    
    def tearDown(self):
        self.players.clear()
        self.players_diff_order.clear() 

if __name__ == '__main___':
    unittest.main()
