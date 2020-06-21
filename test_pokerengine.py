import unittest

import constants as con
import pokerengine as pe
import test_hand_constants as hc

class TestHandRankings(unittest.TestCase):
    
    def test_high_card(self):
        rank_desc = 'high card'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.high_card), result)

    def test_pair(self):
        rank_desc = 'pair'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.pair), result)
    
    def test_two_pair(self):
        rank_desc = 'two pair'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.two_pair), result)

    def test_trips(self):
        rank_desc = 'trips'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.trips), result)

    def test_straight(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.straight), result)

    # A2345
    def test_straight_wheel(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.straight_wheel), result)

    # 10JQKA
    def test_straight_broadway(self):
        rank_desc = 'straight'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.straight_broadway), result)

    def test_flush(self):
        rank_desc = 'flush'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.flush), result)

    def test_full_house(self):
        rank_desc = 'full house'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.full_house), result)
    
    def test_quads(self):
        rank_desc = 'quads'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.quads), result)

    def test_straight_flush(self):
        rank_desc = 'straight flush'
        result = (rank_desc, con.RANKING[rank_desc])
        self.assertEqual(pe._hand_rank(hc.straight_flush), result)

class TestWinningHand(unittest.TestCase):

    def test_pair_vs_trips(self):
        players = []
        
        players.append(hc.pair)
        players.append(hc.trips)

        _winning_desc = 'trips'
        self.assertEqual(pe.winninghand(players),(hc.trips, _winning_desc))
    
    def test_multiple_players(self):
        players = []
        players.append(hc.pair)
        players.append(hc.two_pair)
        players.append(hc.trips)
        players.append(hc.full_house)

        players_diff_order = []
        players_diff_order.append(hc.full_house)
        players_diff_order.append(hc.trips)
        players_diff_order.append(hc.two_pair)
        players_diff_order.append(hc.pair)

        _winning_desc = 'full house'
        result = (hc.full_house, _winning_desc)
        self.assertEqual(pe.winninghand(players), result)
        self.assertEqual(pe.winninghand(players_diff_order), result)


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

        _winning_desc = 'flush'
        result = (hc.flush_same_rank_win, _winning_desc)
        self.assertEqual(pe.winninghand(players), result)
    
    # NOTE: have to copy the same hand in the test due to
    # _same_rank_winning_hand() removing cards
    # TODO - this may need to be fixed
    def test_same_ranking_flush_diff_order(self):
        players = []
        players.append(hc.flush_same_rank_win_do)
        players.append(hc.flush_same_rank_do)

        _winning_desc = 'flush'
        result = (hc.flush_same_rank_win_do, _winning_desc)
        self.assertEqual(pe.winninghand(players), result)


    def test_tied_hand(self):
        pass

if __name__ == '__main___':
    unittest.main()
