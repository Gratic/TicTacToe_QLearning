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
        with self.assertRaises(ValueError):
            self.board.play_if_possible_or_do_nothing(x, 1, 0)
    
    @parameterized.expand([0, 1, 2])
    def test_play_if_possible_or_do_nothing_posX_true(self, x):
        self.board.play_if_possible_or_do_nothing(x, 1, 0)
        
    @parameterized.expand([-2, -1, 3, 4])
    def test_play_if_possible_or_do_nothing_posY_false(self, y):
        with self.assertRaises(ValueError):
            self.board.play_if_possible_or_do_nothing(1, y, 0)
        
    @parameterized.expand([0, 1, 2])
    def test_play_if_possible_or_do_nothing_posY_true(self, y):
        self.board.play_if_possible_or_do_nothing(1, y, 0)
    
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
        with self.assertRaises(ValueError):
            self.board.play_if_possible_or_do_nothing(x, y, 0)
    
    def test_play_if_possible_or_do_nothing_fill_all_board_once(self):
        self.assertTrue(self.board.play_if_possible_or_do_nothing(0, 0, 1))
        self.assertEqual(self.board.valid_moves_left, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(len(self.board.valid_moves_left), 8)
        
        self.assertTrue(self.board.play_if_possible_or_do_nothing(0, 1, 1))
        self.assertEqual(self.board.valid_moves_left, [1, 2, 4, 5, 6, 7, 8])
        self.assertEqual(len(self.board.valid_moves_left), 7)

        self.assertTrue(self.board.play_if_possible_or_do_nothing(0, 2, 1))
        self.assertEqual(self.board.valid_moves_left, [1, 2, 4, 5, 7, 8])
        self.assertEqual(len(self.board.valid_moves_left), 6)

        self.assertTrue(self.board.play_if_possible_or_do_nothing(1, 0, 1))
        self.assertEqual(self.board.valid_moves_left, [2, 4, 5, 7, 8])
        self.assertEqual(len(self.board.valid_moves_left), 5)

        self.assertTrue(self.board.play_if_possible_or_do_nothing(1, 1, 1))
        self.assertEqual(self.board.valid_moves_left, [2, 5, 7, 8])
        self.assertEqual(len(self.board.valid_moves_left), 4)

        self.assertTrue(self.board.play_if_possible_or_do_nothing(1, 2, 1))
        self.assertEqual(self.board.valid_moves_left, [2, 5, 8])
        self.assertEqual(len(self.board.valid_moves_left), 3)

        self.assertTrue(self.board.play_if_possible_or_do_nothing(2, 0, 1))
        self.assertEqual(self.board.valid_moves_left, [5, 8])
        self.assertEqual(len(self.board.valid_moves_left), 2)

        self.assertTrue(self.board.play_if_possible_or_do_nothing(2, 1, 1))
        self.assertEqual(self.board.valid_moves_left, [8])
        self.assertEqual(len(self.board.valid_moves_left), 1)

        self.assertTrue(self.board.play_if_possible_or_do_nothing(2, 2, 1))
        self.assertEqual(self.board.valid_moves_left, [])
        self.assertEqual(len(self.board.valid_moves_left), 0)

    
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
    def test_coords_to_cell_raises_Value_Error(self, x, y):
        with self.assertRaises(ValueError):
            self.board.coords_to_cell(x, y)
    
    @parameterized.expand([(0, 0),
                           (1, 0),
                           (2, 0),
                           (0, 1),
                           (1, 1),
                           (2, 1),
                           (0, 2),
                           (1, 2),
                           (2, 2)])
    def test_coords_to_cell_good_values(self, x, y):
            self.assertEqual(self.board.coords_to_cell(x, y), x + y*3)