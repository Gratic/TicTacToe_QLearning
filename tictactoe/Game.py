from .Board import Board

class Game():
    def __init__(self) -> None:
        self.player1: int = 1
        self.player2: int = 2
        self.board: Board = Board()
        self.current_player = self.player1
        self.game_ended = False
        self.winner = None
        
    def play_if_possible_or_do_nothing(self, posX: int, posY: int) -> bool:
        '''
        Automatically switch the player that plays if the move is correct.
        Also check for winner after each move.
        '''
        if self.game_ended:
            return False
        
        move_is_valid = self.board.play_if_possible_or_do_nothing(posX, posY, self.current_player)
        
        if move_is_valid:
            winner = self.board.get_board_winner()
            if winner != 0:
                self.winner = winner
                self.game_ended = True
            else:
                self.game_ended = self.board.is_board_full()
            
            if self.current_player == self.player1:
                self.current_player = self.player2
            else:
                self.current_player = self.player1
        
        return move_is_valid
    
    def is_game_ended(self):
        return self.game_ended
    
    def get_winner(self):
        return self.winner
    
    def restart(self):
        self.board = Board()
        self.current_player = self.player1
        self.game_ended = False
        self.winner = None
    
    def get_board(self):
        return self.board
    
    def get_raw_board(self):
        return self.board.get_raw_board()
    
    def get_player(self):
        return self.current_player
    
    def get_valid_moves_left(self):
        return self.board.get_valid_moves_left()