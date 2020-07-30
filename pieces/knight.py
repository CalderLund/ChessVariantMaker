from pieces.piece import Piece
from typing import Tuple, Union, List
from board import Board
from pieces.squares import EmptySquare

class Knight(Piece):

    def __init__(self, colour: str, team_colours: List[str] = None):
        super().__init__("knight", "N", 3, colour, team_colours)

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Board) -> List[str]:
        valid = []

        original_position = Board.translate_pos(position)

        
        pos = original_position
        #all move options
        pos1 = (pos[0]+1, pos[1]+2)
        pos2 = (pos[0]-1, pos[1]+2)
        pos3 = (pos[0]-2, pos[1]+1)
        pos4 = (pos[0]-2, pos[1]-1)
        pos5 = (pos[0]-1, pos[1]-2)
        pos6 = (pos[0]+1, pos[1]-2)
        pos7 = (pos[0]+2, pos[1]-1)
        pos8 = (pos[0]+2, pos[1]+1)
        #moves in a list
        moveOptionList = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8]

        #checking all possible moves
        for squares in moveOptionList:
            if not board.valid_square(squares) or \
                        (not isinstance(board[squares], EmptySquare) and board[squares].get_colour() in self._team_colours):
                    continue
            if board.valid_square(squares) and \
                    not isinstance(board[squares], EmptySquare) and \
                    board[squares].get_colour() not in self._team_colours:
                valid.append(squares)
                continue
            valid.append(squares)

        return valid

if __name__ == "__main__":
    board = Board()

    board["C7"] = Knight("white")
    board["D5"] = Knight("white")
    board["F4"] = Knight("black")

    print(Board(invalid_squares = board["C7"].valid_moves("C7", board)))
    print(Board(invalid_squares = board["D5"].valid_moves("D5", board)))
    print(Board(invalid_squares = board["F4"].valid_moves("F4", board)))
