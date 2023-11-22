from typing import List

class Board():
    '''
    This class represent a Board.
    Has capabilities to find the winner or tell when the game should be over.
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    '''
    def __init__(self) -> None:
        self.board: List[int] = [None] * 9
        self.playNumber = 0
    
    def play_if_possible_or_do_nothing(self, posX: int, posY: int, player: int) -> bool:
        if posX < 0 or posX > 2:
            return False
        
        if posY < 0 or posY > 2:
            return False
        
        coords: int = posX + posY*3
        
        if self.board[coords] != None:
           return False

        self.board[coords] = player
        self.playNumber += 1
        return True
    
    def get_board_winner(self) -> int:
        if self.playNumber < 3:
            return 0
        
        column_win = self._check_any_column_winning()
        if column_win != 0:
            return column_win
        
        line_win = self._check_any_line_winning()
        if line_win != 0:
            return line_win
        
        diag_win = self._check_any_diagonal_winning()
        if diag_win != 0:
            return diag_win

        return 0
        
    def is_board_full(self) -> bool:
        return self.playNumber == 9
        
    def get_raw_board(self) -> List[int]:
        return self.board
        
    def _check_column_is_winning(self, posX: int) -> int:
        if self.board[posX] == None:
            return 0
        
        if self.board[posX] == self.board[posX+3] and self.board[posX] == self.board[posX + 6]:
            return self.board[posX]
        
        return 0   
    
    def _check_any_column_winning(self) -> int:
        for x in range(0, 3):
            column_return: int = self._check_column_is_winning(x)
            if column_return != 0:
                return column_return
        
        return 0
    
    def _check_line_is_winning(self, posY: int) -> int:
        if self.board[posY*3] == None:
            return 0
        
        if self.board[posY*3] == self.board[posY*3+1] and self.board[posY*3] == self.board[posY*3 + 2]:
            return self.board[posY*3]

        return 0
    
    def _check_any_line_winning(self) -> int:
        for y in range(0, 3):
            line_return: int = self._check_line_is_winning(y)
            if line_return != 0:
                return line_return
        
        return 0
    
    def _check_any_diagonal_winning(self) -> int:
        if self.board[0] == None and self.board[2] == None:
            return 0
        
        if self.board[0] != None and self.board[0] == self.board[4] and self.board[0] == self.board[8]:
            return self.board[0]
        
        if self.board[2] != None and self.board[2] == self.board[4] and self.board[2] == self.board[6]:
            return self.board[2]
        
        return 0
        
        