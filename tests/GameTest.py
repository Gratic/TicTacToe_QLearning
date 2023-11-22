import unittest
from parameterized import parameterized
from tictactoe import Game

class GameTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def setUp(self) -> None:
        self.game = Game()
    
    def test_play_if_possible_or_do_nothing_game_ended(self):
        self.game.game_ended = True
        self.assertFalse(self.game.play_if_possible_or_do_nothing(0,0))
        
    def test_play_if_possible_or_do_nothing_switch_player(self):
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,0))
        self.assertEqual(self.game.get_raw_board()[0], self.game.player1)
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,0))
        self.assertEqual(self.game.get_raw_board()[1], self.game.player2)
    
    def test_play_if_possible_or_do_nothing_switch_player_2(self):
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,0))
        self.assertEqual(self.game.get_raw_board()[0], self.game.player1)
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,0))
        self.assertEqual(self.game.get_raw_board()[1], self.game.player2)
        self.assertTrue(self.game.play_if_possible_or_do_nothing(2,0))
        self.assertEqual(self.game.get_raw_board()[2], self.game.player1)
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,1))
        self.assertEqual(self.game.get_raw_board()[3], self.game.player2)
    
    def test_play_if_possible_or_do_nothing_draw(self):
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,2))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(2,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,2))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(2,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(2,2))
        
        self.assertTrue(self.game.is_game_ended())
        self.assertEqual(self.game.get_winner(), None, f"Should produce Draw (None) but produced win of {self.game.get_winner()}.")
    
    def test_play_if_possible_or_do_nothing_win1(self):
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,2))
        
        self.assertTrue(self.game.is_game_ended())
        self.assertEqual(self.game.get_winner(), 1, f"Should produce win of player 1 but produced {self.game.get_winner()}.")
    
    def test_play_if_possible_or_do_nothing_win2(self):
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(2,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,2))
        
        self.assertTrue(self.game.is_game_ended())
        self.assertEqual(self.game.get_winner(), 2, f"Should produce win of player 2 but produced {self.game.get_winner()}.")
    
    def test_play_if_possible_or_do_nothing_same_cell(self):
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,0))
        self.assertFalse(self.game.play_if_possible_or_do_nothing(0,0))
    
    def test_restart_ok1(self):
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,0))
        self.assertEqual(self.game.get_player(), self.game.player2)
        self.assertEqual(self.game.get_raw_board()[0], self.game.player1)
        
        self.game.restart()
        
        self.assertEqual(self.game.get_player(), self.game.player1)
        self.assertEqual(self.game.get_raw_board()[0], None)
    
    def test_restart_ok2(self):
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(0,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,1))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(2,0))
        self.assertTrue(self.game.play_if_possible_or_do_nothing(1,2))
        
        self.assertTrue(self.game.is_game_ended())
        self.assertEqual(self.game.get_winner(), 2, f"Should produce win of player 2 but produced {self.game.get_winner()}.")
        
        self.game.restart()
        
        self.assertEqual(self.game.get_player(), self.game.player1)
        self.assertEqual(self.game.get_raw_board()[0], None)
        self.assertEqual(self.game.get_winner(), None)
        self.assertFalse(self.game.is_game_ended())