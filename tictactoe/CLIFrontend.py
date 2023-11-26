from .Game import Game
from .QFunction import QFunction
from .QState import QState
import random

class CLIFrontend():
    def __init__(self, game: Game) -> None:
        self.game = game
        self.Qfunction = QFunction()
        self.Qfunction.load_json("qfunction_10M_2.json")
    
    def main(self):
        while True:
            self.gameloop()

    def gameloop(self):
        while not self.game.is_game_ended():
            self._display_board()
            move_valid = False
            while not move_valid:
                posX, posY = None, None
                
                if self.game.get_player() == self.game.player1:
                    posX, posY = self._ask_position()
                else:
                    action = self.Qfunction.greedy_policy(QState(self.game.get_player(), self.game.get_board()), self.game.get_valid_moves_left())
                    if action not in self.game.get_valid_moves_left():
                        action = random.choice(self.game.get_valid_moves_left())
                    
                    posX, posY = action%3, action//3
                    
                move_valid = self.game.play_if_possible_or_do_nothing(posX, posY)
                
                if not move_valid:
                    print("Input is invalid. Please play again.")
        
        self._display_board()
        
        winner = self.game.get_winner()
        if winner ==  None:
            print("Draw!")
        else:
            print(f"Player{winner} has won the game!")
            
        print("Press enter to restart the game and 'q' to leave.")
        c = input("")
        
        if c == "q":
            exit(0)
        
        self.game.restart()

    def _ask_position(self) -> tuple[int, int]:
        raw_posX = input(f"(Player{self.game.get_player()}) your column (0 to 2):")
        while not raw_posX.isdigit():
            print("Input is not a valid integer.")
            raw_posX = input(f"(Player{self.game.get_player()}) your column (0 to 2):")
                
        raw_posY = input(f"(Player{self.game.get_player()}) your line (0 to 2):")
        while not raw_posY.isdigit():
            print("Input is not a valid integer.")
            raw_posY = input(f"(Player{self.game.get_player()}) your line (0 to 2):")
                
        posX = int(raw_posX)
        posY = int(raw_posY)
        return posX,posY
    
    def _display_board(self):
        print(f"    0 | 1 | 2 ")
        print("   -"+"-"*11)
        print(f" 0 | {self._get_player_character(0)} | {self._get_player_character(1)} | {self._get_player_character(2)} ")
        print("---|"+"-"*11)
        print(f" 1 | {self._get_player_character(3)} | {self._get_player_character(4)} | {self._get_player_character(5)} ")
        print("---|"+"-"*11)
        print(f" 2 | {self._get_player_character(6)} | {self._get_player_character(7)} | {self._get_player_character(8)} ")
    
    def _get_player_character(self, pos: int) -> str:
        board = self.game.get_raw_board()
        if board[pos] == None:
            return " "
        
        if board[pos] == 1:
            return "X"
        
        if board[pos] == 2:
            return "O"