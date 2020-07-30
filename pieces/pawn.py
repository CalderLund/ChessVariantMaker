from pieces.piece import Piece
from typing import Tuple, Union, List
from board import Board
from constants import NORTH, SOUTH, EAST, WEST
from pieces.squares import EmptySquare


class Pawn(Piece):
    def __init__(self, direction: int, colour: str, team_colours: List[str] = None, moved: bool = False, enpassable = False):
        super().__init__("pawn", "P", 1, colour, team_colours)
        self._direction = direction
        self._moved = moved
        self._enpassable = enpassable

    def get_enpassable(self):
        return self._enpassable

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Board) -> List[str]:
        valid = []

        # Get position in tuple format
        original_pos = Board.translate_pos(position)
        
        pos = original_pos
        # going up
        if self._direction == NORTH:
            pos_up = (pos[0]+1, pos[1])
            pos_up_right = (pos[0]+1, pos[1]+1)
            pos_up_left = (pos[0]+1, pos[1]-1)
            pos_up_two = (pos[0]+2, pos[1])
            enpassant_right = (pos[0], pos[1]+1)
            enpassant_left = (pos[0], pos[1]-1)
            
        # going right
        elif self._direction == EAST:
            pos_up = (pos[0], pos[1]+1)
            pos_up_right = (pos[0]-1, pos[1]+1)
            pos_up_left = (pos[0]+1, pos[1]+1)
            pos_up_two = (pos[0], pos[1]+2)
            enpassant_right = (pos[0]-1, pos[1])
            enpassant_left = (pos[0]+1, pos[1])

        # going down
        elif self._direction == SOUTH:
            pos_up = (pos[0]-1, pos[1])
            pos_up_right = (pos[0]+1, pos[1]-1)
            pos_up_left = (pos[0]-1, pos[1]+1)
            pos_up_two = (pos[0]-2, pos[1])
            enpassant_right = (pos[0], pos[1]-1)
            enpassant_left = (pos[0], pos[1]+1)
             
        # going left
        elif self._direction == WEST:
            pos_up = (pos[0], pos[1]-1)
            pos_up_right = (pos[0]+1, pos[1]-1)
            pos_up_left = (pos[0]-1, pos[1]-1)
            pos_up_two = (pos[0], pos[1]-2)
            enpassant_right = (pos[0]+1, pos[1])
            enpassant_left = (pos[0]-1, pos[1])

        else:
            raise ValueError("direction not a recognized direction")

        # normal moves
        if board.valid_square(pos_up) and isinstance(board[pos_up], EmptySquare):
                valid.append(pos_up)

        if board.valid_square(pos_up_right) and \
                not isinstance(board[pos_up_right], EmptySquare) and \
                board[pos_up_right].get_colour() not in self._team_colours:
                valid.append(pos_up_right)

        if board.valid_square(pos_up_left) and \
                not isinstance(board[pos_up_left], EmptySquare) and \
                board[pos_up_left].get_colour() not in self._team_colours:
                valid.append(pos_up_left)

        if pos_up in valid and not self._moved:
            if board.valid_square(pos_up_two) and isinstance(board[pos_up_two], EmptySquare):
                valid.append(pos_up_two)

        # en passant
        # first line is for 2 player, 2nd line does 4 player 
        if board.valid_square(enpassant_right) and \
                ((isinstance(board[enpassant_right], Pawn) and
                  board[enpassant_right].get_enpassable() and
                  board[enpassant_right].get_colour not in self._team_colours) or
                 (isinstance(board[pos_up], Pawn) and board[pos_up].get_enpassable() and
                  board[pos_up].get_colour not in self._team_colours and
                  (board[pos_up]._direction == self._direction-1 or
                   board[pos_up]._direction == self._direction+3)) and
                 isinstance(board[pos_up_right], EmptySquare)):
            valid.append(pos_up_right)
        if board.valid_square(enpassant_left) and \
                ((isinstance(board[enpassant_left], Pawn) and
                  board[enpassant_left].get_enpassable() and
                  board[enpassant_left].get_colour not in self._team_colours) or
                 (isinstance(board[pos_up], Pawn) and board[pos_up].get_enpassable() and
                  board[pos_up].get_colour not in self._team_colours and
                  (board[pos_up]._direction == self._direction+1 or
                   board[pos_up]._direction == self._direction-3)) and
                 isinstance(board[pos_up_left], EmptySquare)):
            valid.append(pos_up_left)
        return valid


# testing
if __name__ == "__main__":
    board = Board()
    board["G7"] = Pawn(SOUTH, "S", enpassable=False)
    board["A6"] = Pawn(NORTH, "N", moved=True)
    board["B6"] = Pawn(SOUTH, "S", enpassable=True)

    board["G6"] = Pawn(WEST, "W", enpassable=True)
    board["G5"] = Pawn(NORTH, "N", enpassable=False)
    board["G4"] = Pawn(WEST, "W", moved=False)
    board["B4"] = Pawn(EAST, "E", moved=False)

    board["E2"] = Pawn(NORTH, "N", enpassable=False)
    board["F3"] = Pawn(SOUTH, "S", moved=True)
    board["D3"] = Pawn(SOUTH, "N", moved=True)

    print(board.__str__(colours=True))
    print("A6", "\n", Board(invalid_squares=board["A6"].valid_moves("A6", board)))
    print("G7", "\n", Board(invalid_squares=board["G7"].valid_moves("G7", board)))
    print("G5", "\n", Board(invalid_squares=board["G5"].valid_moves("G5", board)))
    print("E2", "\n", Board(invalid_squares=board["E2"].valid_moves("E2", board)))
    print("G4", "\n", Board(invalid_squares=board["G4"].valid_moves("G4", board)))
    print("B4", "\n", Board(invalid_squares=board["B4"].valid_moves("B4", board)))


