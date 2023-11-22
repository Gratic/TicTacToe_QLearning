import json
import random
from .QState import QState

class QFunction():
    def __init__(self, random_seed = 0) -> None:
        self.Qtable:dict[int, dict[int,float]] = self.initialize_qtable()
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
    
    def epsilon_greedy_policy(self, state: QState, epsilon: float) -> int:
        if self.random.random() < epsilon:
            return self.random.randint(0, 8)
        else:
            return self.greedy_policy(state)
    
    def get_state_action_value(self, state: QState, action: int) -> float:
        return self.Qtable[state][action]
    
    def set_state_action_value(self, state: QState, action: int, value: float):
        self.Qtable[state][action] = value
    
    def to_json(self) -> str:
        return json.dumps(self.Qtable)
    
    def load_json(self, json_str: str) -> bool:
        obj = json.loads(json_str)
        
        if not isinstance(obj, dict[int, tuple[int,float]]):
            return False
        
        self.Qtable = obj
        return True
    
    def initialize_qtable(self) -> dict[int, dict[int, float]]:
        qtable = dict()
        for i in range(0, 524288):
            qtable[i] = self._init_state_Qtable()
        return qtable

    def _init_state_Qtable(self) -> dict[int, float]:
        state = dict()
        for i in range(0, 9):
            state[i] = 0
        return state
        