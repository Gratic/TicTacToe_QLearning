from .Board import Board
from typing import List

class QState():
    def __init__(self, player: int, board: Board) -> None:
        self.hash = self.compute_hash(self._convert_board(player, board))
    
    @staticmethod
    def _convert_board(player: int, board: Board) -> List[int]:
        converted_board = []
        for i in range(0,9):
            if board.get_raw_board()[i] == player:
                converted_board.append(1)
            elif board.get_raw_board()[i] == None:
                converted_board.append(0)
            elif board.get_raw_board()[i] != player:
                converted_board.append(2)
        
        return converted_board
    
    def __hash__(self) -> int:
        return self.hash

    @staticmethod
    def compute_hash(converted_board: List[int]):
        bit_string = ''
    
        for number in converted_board:
            # Extract the first two bits using bitwise AND and bit shifting
            first_bit = number & 1       # Extracts the LSB
            second_bit = (number & 2) >> 1  # Extracts the second bit and shifts it to the LSB position

            # Append the bits to the bit string
            bit_string += str(first_bit) + str(second_bit)
        
        # Convert the bit string to an integer
        concatenated_bits = int(bit_string[::-1], 2)
        
        return concatenated_bits
    
    def __eq__(self, __value: object) -> bool:
        return self.__hash__() == __value.__hash__()