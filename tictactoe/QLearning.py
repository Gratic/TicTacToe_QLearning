from .QFunction import QFunction
from .QState import QState
from .Game import Game
import random

class QLearning():
    def __init__(self) -> None:
        self.Qfunction = QFunction()
    
    def training(self, max_episode: int, decay: str, lr: float, discount_rate: float) -> None:
        eps_decay = self._linear_decay
        game = Game()
        
        if decay == "quadratic":
            eps_decay = self._quadratic_decay
        
        for x in range(max_episode):
            epsilon = eps_decay(x, max_episode)
            
            if x%1000 == 0:
                (num_win, num_draw, num_no_valid_move) = self.evaluate(100)
                print(f"{x}/{max_episode}".ljust(10), f"| {int((x/max_episode)*100)}%".ljust(6), f"| wr={num_win}%, dr={num_draw}%, fail={num_no_valid_move}")
            
            while not game.is_game_ended():
                state_t = QState(game.player1, game.get_board())
                reward = .0
                
                valid_move = False
                tries_left = 10
                while not valid_move:
                    if tries_left > 0:
                        action_t = self.Qfunction.epsilon_greedy_policy(state_t, epsilon)
                        tries_left -= 1
                    else:
                        action_t = random.randint(0, 8)
                        
                    posX, posY = action_t%3, action_t//3
                    valid_move = game.play_if_possible_or_do_nothing(posX, posY)
                    
                state_tp1 = QState(game.player1, game.get_board())
                action_tp1 = self.Qfunction.greedy_policy(state_tp1)

                if game.is_game_ended():
                    if game.get_winner() == game.player1:
                        reward = 1.
                    elif game.get_winner() == None:
                        reward = .0
                
                if not game.is_game_ended():
                    enemy_valid_move = False
                    while not enemy_valid_move:
                        enemy_valid_move = game.play_if_possible_or_do_nothing(random.randint(0, 2), random.randint(0, 2))
                        
                if game.is_game_ended():
                    if game.get_winner() == game.player2:
                        reward = -1.
                    elif game.get_winner() == None:
                        reward = .0
                        
                val = self.Qfunction.get_state_action_value(state_t, action_t)
                valp1 = self.Qfunction.get_state_action_value(state_tp1, action_tp1)
                self.Qfunction.set_state_action_value(state_t, action_t, val + lr * (reward + discount_rate * valp1 - val))
            
            game.restart()
            
        (num_win, num_draw, num_no_valid_move) = self.evaluate(10000)
        print(f"{x}/{max_episode}".ljust(10), f"| {int((x/max_episode)*100)}%".ljust(6), f"| wr={int((num_win/10000)*100)}%, dr={int((num_draw/10000)*100)}%, fail={num_no_valid_move}")
    
    def evaluate(self, num_games: int):
        num_wins = 0
        num_draw = 0
        num_no_valid_move = 0
        game = Game()
        
        for _ in range(num_games):
            while not game.is_game_ended():
                if game.get_player() == game.player1:
                    state = QState(game.player1, game.get_board())
                    action = self.Qfunction.greedy_policy(state)
                    posX, posY = action%3, action//3
                    
                    valid_move = game.play_if_possible_or_do_nothing(posX, posY)
                    if not valid_move:
                        num_no_valid_move += 1
                        
                    while not valid_move:
                        valid_move = game.play_if_possible_or_do_nothing(random.randint(0, 2), random.randint(0, 2))
                        
                else:
                    valid_move = False
                    while not valid_move:
                        valid_move = game.play_if_possible_or_do_nothing(random.randint(0, 2), random.randint(0, 2))

            if game.get_winner() == None:
                num_draw += 1
            elif game.get_winner() == game.player1:
                num_wins += 1
            
            game.restart()
        
        return (num_wins, num_draw, num_no_valid_move)
            
    def _linear_decay(self, x:int, max_x:int) -> float:
        return 1 - float(x)/float(max_x)

    def _quadratic_decay(self, x:int, max_x:int) -> float:
        return self._linear_decay(x, max_x)**2