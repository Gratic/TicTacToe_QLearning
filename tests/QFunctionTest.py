import unittest
from tictactoe import QFunction, QState, Board

class QFunctionTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def setUp(self) -> None:
        self.Qfunction = QFunction()
    
    def test_get_state_action_value_empty(self):
        self.assertEqual(self.Qfunction.get_state_action_value(QState(1, Board()), 0), 0)
        self.assertEqual(self.Qfunction.Qtable, {0: {0: 0, 1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}})
        
    def test_set_state_action_value_empty(self):
        self.Qfunction.set_state_action_value(QState(1, Board()), 0, 1)
        self.assertEqual(self.Qfunction.Qtable, {0: {0: 1, 1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}})
    
    def test_init_state_Qtable(self):
        self.assertEqual(QFunction._init_state_Qtable(), {0: 0, 1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0})
    
    def test_greedy_policy(self):
        self.Qfunction.set_state_action_value(QState(1, Board()), 5, 1)
        self.assertEqual(self.Qfunction.greedy_policy(QState(1, Board())), 5)