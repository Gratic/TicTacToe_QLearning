from .Board import Board
from typing import List
from copy import deepcopy

class QState():
    def __init__(self, player: int, board: Board) -> None:
        self.player = player
        self.board: List[int] = deepcopy(board.get_raw_board())
        self.converted_board = self._convert_board()
        
    def _convert_board(self) -> List[int]:
        converted_board = []
        for i in range(0,9):
            if self.board[i] == self.player:
                converted_board.append(1)
            elif self.board[i] == None:
                converted_board.append(0)
            elif self.board[i] != self.player:
                converted_board.append(2)
        
        return converted_board
    
    def __hash__(self) -> int:
        bit_string = ''
    
        for number in self.converted_board:
            # Extract the first two bits using bitwise AND and bit shifting
            first_bit = (number & 2) >> 1  # Extracts the second bit and shifts it to the LSB position
            second_bit = number & 1       # Extracts the LSB

            # Append the bits to the bit string
            bit_string += str(first_bit) + str(second_bit)
        
        # Convert the bit string to an integer
        concatenated_bits = int(bit_string, 2)
        
        return concatenated_bits
    
    def __eq__(self, __value: object) -> bool:
        return self.__hash__() == __value.__hash__()