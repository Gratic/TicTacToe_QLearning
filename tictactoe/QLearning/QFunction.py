import json
import random
from .QState import QState
from typing import List
from collections import defaultdict

class QFunction():
    def __init__(self, random_seed = 0) -> None:
        self.Qtable:dict[int, dict[int,float]] = defaultdict(self._init_state_Qtable)
        self.random = random.Random()
        
        if random_seed != 0:
            self.random.seed(random_seed)
    
    def greedy_policy(self, state: QState, valid_moves: List[int]) -> int:
        max_a = -1
        max_v = -1
        for i in range(0,9):
            if i in valid_moves and self.Qtable[state.hash][i] > max_v:
                max_v = self.Qtable[state.hash][i]
                max_a = i
        return max_a
    
    def epsilon_greedy_policy(self, state: QState, epsilon: float, valid_moves: List[int]) -> int:
        if self.random.random() < epsilon:
            return self.random.choice(valid_moves)
        else:
            return self.greedy_policy(state, valid_moves)
    
    def get_state_action_value(self, state: QState, action: int) -> float:
        return self.Qtable[state.hash][action]
    
    def set_state_action_value(self, state: QState, action: int, value: float):
        self.Qtable[state.hash][action] = value
    
    def save_to_json(self, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(json.dumps(self.Qtable))
    
    def load_json(self, filename: str) -> bool:
        obj = None
        with open(filename, "r") as f:
            obj = json.loads(f.read())
        
        if not isinstance(obj, dict):
            return False
        
        for key in obj.keys():
            dc = defaultdict(lambda: 0.)
            dc.update({int(keyy): obj[key][keyy] for keyy in obj[key].keys()})
            obj[key] = dc
        
        self.Qtable = defaultdict(self._init_state_Qtable)
        self.Qtable.update({int(key): obj[key] for key in obj.keys()})
        
        return True

    @staticmethod
    def _init_state_Qtable() -> dict[int, float]:
        state = defaultdict(lambda: 0.)
        return state