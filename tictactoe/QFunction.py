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
    
    def greedy_policy(self, state: QState) -> int:
        max_a = 0
        max_v = 0
        for i in range(0,9):
            if self.Qtable[state][i] > max_v:
                max_v = self.Qtable[state][i]
                max_a = i
        return max_a
    
    def epsilon_greedy_policy(self, state: QState, epsilon: float, valid_moves: List[int]) -> int:
        if self.random.random() < epsilon:
            return self.random.choice(valid_moves)
        else:
            return self.greedy_policy(state)
    
    def get_state_action_value(self, state: QState, action: int) -> float:
        return self.Qtable[state][action]
    
    def set_state_action_value(self, state: QState, action: int, value: float):
        self.Qtable[state][action] = value
    
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
            obj[key] = {int(keyy): obj[key][keyy] for keyy in obj[key].keys()}
        
        self.Qtable = {int(key): obj[key] for key in obj.keys()}
        return True
    
    # def initialize_qtable(self) -> dict[int, dict[int, float]]:
    #     qtable = dict()
    #     for i in range(0, 524288):
    #         qtable[i] = self._init_state_Qtable()
    #     return qtable

    @staticmethod
    def _init_state_Qtable() -> dict[int, float]:
        state = dict()
        for i in range(0, 9):
            state[i] = 0
        return state