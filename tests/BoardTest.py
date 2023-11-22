import unittest
from parameterized import parameterized
from tictactoe import Board

class BoardTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def setUp(self) -> None:
        self.board = Board()
    
    def tearDown(self) -> None:
        del self.board
        self.board = None
    
    @parameterized.expand([-2, -1, 3, 4])
    def test_play_if_possible_or_do_nothing_posX_false(self, x):
        self.assertFalse(self.board.play_if_possible_or_do_nothing(x, 1, 0), f"x={x} should produce a False result.")
    
    @parameterized.expand([0, 1, 2])
    def test_play_if_possible_or_do_nothing_posX_true(self, x):
        self.assertTrue(self.board.play_if_possible_or_do_nothing(x, 1, 0), f"x={x} should produce a True result.")
        
    @parameterized.expand([-2, -1, 3, 4])
    def test_play_if_possible_or_do_nothing_posY_false(self, y):
        self.assertFalse(self.board.play_if_possible_or_do_nothing(1, y, 0), f"y={y} should produce a False result.")
        
    @parameterized.expand([0, 1, 2])
    def test_play_if_possible_or_do_nothing_posX_true(self, y):
        self.assertTrue(self.board.play_if_possible_or_do_nothing(1, y, 0), f"y={y} should produce a True result.")
    
    @parameterized.expand([(-1, -1),
                           (-1, 0),
                           (-1, 1),
                           (-1, 2),
                           (-1, 3),
                           (3, -1),
                           (3, 3),
                           (3, 0),
                           (3, 1),
                           (3, 2)])
    def test_play_if_possible_or_do_nothing_posX_posY(self, x, y):
        self.assertFalse(self.board.play_if_possible_or_do_nothing(x, y, 0), f"The ({x},{y}) produce a True answer when it should produce False.")
    
    def test_play_if_possible_or_do_nothing_fill_all_board_once(self):
        self.board.play_if_possible_or_do_nothing(0, 0, 1)
        self.board.play_if_possible_or_do_nothing(0, 1, 1)
        self.board.play_if_possible_or_do_nothing(0, 2, 1)
        self.board.play_if_possible_or_do_nothing(1, 0, 1)
        self.board.play_if_possible_or_do_nothing(1, 1, 1)
        self.board.play_if_possible_or_do_nothing(1, 2, 1)
        self.board.play_if_possible_or_do_nothing(2, 0, 1)
        self.board.play_if_possible_or_do_nothing(2, 1, 1)
        self.board.play_if_possible_or_do_nothing(2, 2, 1)
    
    @parameterized.expand([(0,0),
                           (0,1),
                           (0,2),
                           (1,0),
                           (1,1),
                           (1,2),
                           (2,0),
                           (2,1),
                           (2,2)])
    def test_play_if_possible_or_do_nothing_fill_same_cell(self, x, y):
        self.board.play_if_possible_or_do_nothing(x, y, 0)
        self.assertFalse(self.board.play_if_possible_or_do_nothing(x, y, 0), f"({x},{y}) produce a True when it should produce False.")
    
    def test_play_if_possible_or_do_nothing_actually_fills_board(self):
        self.board.play_if_possible_or_do_nothing(0, 0, 1)
        self.assertEqual(self.board.get_raw_board()[0], 1)
    
    def test_get_board_winner_no_winner(self):
        self.assertEqual(self.board.get_board_winner(), 0)
    
    def test_get_board_winner_winner_column1(self):
        self.board.play_if_possible_or_do_nothing(0, 0, 1)
        self.board.play_if_possible_or_do_nothing(0, 1, 1)
        self.board.play_if_possible_or_do_nothing(0, 2, 1)
        self.assertEqual(self.board._check_any_column_winning(), 1)
        self.assertEqual(self.board.get_board_winner(), 1)
    
    def test_get_board_winner_winner_column2(self):
        self.board.play_if_possible_or_do_nothing(1, 0, 1)
        self.board.play_if_possible_or_do_nothing(1, 1, 1)
        self.board.play_if_possible_or_do_nothing(1, 2, 1)
        self.assertEqual(self.board._check_any_column_winning(), 1)
        self.assertEqual(self.board.get_board_winner(), 1)
    
    def test_get_board_winner_winner_column3(self):
        self.board.play_if_possible_or_do_nothing(2, 0, 1)
        self.board.play_if_possible_or_do_nothing(2, 1, 1)
        self.board.play_if_possible_or_do_nothing(2, 2, 1)
        self.assertEqual(self.board._check_any_column_winning(), 1)
        self.assertEqual(self.board.get_board_winner(), 1)
    
    def test_get_board_winner_winner_line1(self):
        self.board.play_if_possible_or_do_nothing(0, 0, 1)
        self.board.play_if_possible_or_do_nothing(1, 0, 1)
        self.board.play_if_possible_or_do_nothing(2, 0, 1)
        print(self.board.get_raw_board())
        self.assertEqual(self.board._check_any_line_winning(), 1)
        self.assertEqual(self.board.get_board_winner(), 1)
    
    def test_get_board_winner_winner_line2(self):
        self.board.play_if_possible_or_do_nothing(0, 1, 1)
        self.board.play_if_possible_or_do_nothing(1, 1, 1)
        self.board.play_if_possible_or_do_nothing(2, 1, 1)
        self.assertEqual(self.board._check_any_line_winning(), 1)
        self.assertEqual(self.board.get_board_winner(), 1)
    
    def test_get_board_winner_winner_line3(self):
        self.board.play_if_possible_or_do_nothing(0, 2, 1)
        self.board.play_if_possible_or_do_nothing(1, 2, 1)
        self.board.play_if_possible_or_do_nothing(2, 2, 1)
        self.assertEqual(self.board._check_any_line_winning(), 1)
        self.assertEqual(self.board.get_board_winner(), 1)
        
    def test_get_board_winner_winner_diag1(self):
        self.board.play_if_possible_or_do_nothing(0, 0, 1)
        self.board.play_if_possible_or_do_nothing(1, 1, 1)
        self.board.play_if_possible_or_do_nothing(2, 2, 1)
        self.assertEqual(self.board._check_any_diagonal_winning(), 1)
        self.assertEqual(self.board.get_board_winner(), 1)
    
    def test_get_board_winner_winner_diag2(self):
        self.board.play_if_possible_or_do_nothing(2, 0, 1)
        self.board.play_if_possible_or_do_nothing(1, 1, 1)
        self.board.play_if_possible_or_do_nothing(0, 2, 1)
        self.assertEqual(self.board._check_any_diagonal_winning(), 1)
        self.assertEqual(self.board.get_board_winner(), 1)