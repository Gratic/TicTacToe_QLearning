import unittest
from tictactoe import QFunction, QState, Board
from collections import defaultdict
import os
import json

class QFunctionTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def setUp(self) -> None:
        self.QFunction = QFunction()
    
    @classmethod
    def setUpClass(cls) -> None:
        qtable_empty = defaultdict(QFunction._init_state_Qtable)
        with open("empty.json", "w") as f:
            f.write(json.dumps(qtable_empty))
        
        qtable_state_0_action_0 = defaultdict(QFunction._init_state_Qtable)
        qtable_state_0_action_0[0][0] = 5.
        with open("state_0_action_0.json", "w") as f:
            f.write(json.dumps(qtable_state_0_action_0))
    
    @classmethod
    def tearDownClass(cls) -> None:
        os.remove("empty.json")
        os.remove("state_0_action_0.json")
        
        if os.path.exists("empty_test.json"):
            os.remove("empty_test.json")
        
        if os.path.exists("state_0_action_0_test.json"):
            os.remove("state_0_action_0_test.json")
        
    def test_get_state_action_value_empty(self):
        self.assertEqual(self.QFunction.get_state_action_value(QState(1, Board()), 0), 0)
        self.assertEqual(self.QFunction.Qtable, {0: {0: 0}})
        
    def test_set_state_action_value_empty(self):
        self.QFunction.set_state_action_value(QState(1, Board()), 0, 1)
        self.assertEqual(self.QFunction.Qtable, {0: {0: 1}})
    
    def test_init_state_Qtable(self):
        self.assertEqual(QFunction._init_state_Qtable(), {})
    
    def test_greedy_policy(self):
        self.QFunction.set_state_action_value(QState(1, Board()), 5, 1)
        self.assertEqual(self.QFunction.greedy_policy(QState(1, Board())), 5)
        
    def test_save_to_json_empty(self):
        self.QFunction.save_to_json("empty_test.json")
        
        test_file = None
        file = None
        
        self.assertTrue(os.path.exists("empty_test.json"))
        
        with open("empty_test.json", "r") as f:
            test_file = f.read()
        with open("empty.json", "r") as f:
            file = f.read()
            
        self.assertEqual(test_file, file)
        
    def test_save_to_json_state_0_action_0(self):
        board = Board()
        self.QFunction.set_state_action_value(QState(1, board), 0, 5.)
        self.QFunction.save_to_json("state_0_action_0_test.json")
        
        test_file = None
        file = None
        
        self.assertTrue(os.path.exists("state_0_action_0_test.json"))
        
        with open("state_0_action_0_test.json", "r") as f:
            test_file = f.read()
        with open("state_0_action_0.json", "r") as f:
            file = f.read()
            
        self.assertEqual(test_file, file)
    
    def test_load_json_empty(self):
        self.QFunction.load_json("empty.json")
        
        self.assertIsInstance(self.QFunction.Qtable, defaultdict)
        self.assertEqual(len(self.QFunction.Qtable.keys()), 0)
    
    def test_load_json_state_0_action_0(self):
        self.QFunction.load_json("state_0_action_0.json")
        
        self.assertIsInstance(self.QFunction.Qtable, defaultdict)
        self.assertIsInstance(self.QFunction.Qtable[0], defaultdict)
        self.assertEqual(self.QFunction.Qtable[0][0], 5.)
        self.assertEqual(self.QFunction.get_state_action_value(QState(1, Board()), 0), 5.)