import unittest
from tictactoe import QState, Board

class QStateTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def test_convert_board_empty(self):
        board = Board()
        board.board = [None]*9
        self.assertEqual(QState._convert_board(1, board), [0]*9)
    
    def test_convert_board_one_play(self):
        board = Board()
        board.board = [None, 5, None, None, None, None, None, None, None]
        self.assertEqual(QState._convert_board(5, board), [0, 1, 0, 0, 0, 0, 0, 0, 0])
    
    def test_convert_board_one_play_enemy(self):
        board = Board()
        board.board = [None, 5, None, None, None, None, None, None, None]
        self.assertEqual(QState._convert_board(2, board), [0, 2, 0, 0, 0, 0, 0, 0, 0])
    
    def test_convert_board_one_play_both(self):
        board = Board()
        board.board = [None, 5, None, 2, None, None, None, None, None]
        self.assertEqual(QState._convert_board(2, board), [0, 2, 0, 1, 0, 0, 0, 0, 0])
    
    def test_compute_hash_empty(self):
        board = [0]*9
        self.assertEqual(QState.compute_hash(board), 0)
    
    def test_compute_hash_one_play(self):
        board = [1] + [0]*8
        self.assertEqual(QState.compute_hash(board), 1)
    
    def test_compute_hash_two_play(self):
        board = [1] + [2] + [0]*7
        self.assertEqual(QState.compute_hash(board), 9)
        
    def test_hash_empty(self):
        board = Board()
        board.board = [None]*9
        state = QState(1, board)
        self.assertEqual(state.hash, 0)
        
    def test_hash_one(self):
        board = Board()
        board.board = [1] + [None]*8
        state = QState(1, board)
        self.assertEqual(state.hash, 1)
    
    def test_hash_two(self):
        board = Board()
        board.board = [1] + [2] + [None]*7
        state = QState(1, board)
        self.assertEqual(state.hash, 9)
        