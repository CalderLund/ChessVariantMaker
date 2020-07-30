from pieces.piece import Piece
from typing import Tuple, Union, List
from board import Board
from constants import NORTH, SOUTH, EAST, WEST
from pieces.squares import EmptySquare
from pieces.rook import Rook


class Pawn(Piece):
    def __init__(self, direction: int, colour: str, team_colours: List[str] = None, moved: bool = False, enPassable = False):
        super().__init__("pawn", "P", 1, colour, team_colours)
        self._direction = direction
        self._moved = moved
        self.get_enPassable = enPassable

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Board) -> List[str]:
        valid = []

        # Get position in tuple format
        original_pos = Board.translate_pos(position)
        
        pos = original_pos
        # going up
        if self._direction == 1:
            posUp = (pos[0]+1, pos[1])
            posUpRight = (pos[0]+1, pos[1]+1)
            posUpLeft = (pos[0]+1, pos[1]-1)
            posUpTwo = (pos[0]+2, pos[1])
            enPassantCheckRight = (pos[0], pos[1]+1)
            enPassantCheckLeft = (pos[0], pos[1]-1)
            
        #going right
        elif self._direction == 2:
            posUp = (pos[0], pos[1]+1)
            posUpRight = (pos[0]-1, pos[1]+1)
            posUpLeft = (pos[0]+1, pos[1]+1)
            posUpTwo = (pos[0], pos[1]+2)
            enPassantCheckRight = (pos[0]-1, pos[1])
            enPassantCheckLeft = (pos[0]+1, pos[1])
        #going down
        elif self._direction == 3:
            posUp = (pos[0]-1, pos[1])
            posUpRight = (pos[0]+1, pos[1]-1)
            posUpLeft = (pos[0]-1, pos[1]+1)
            posUpTwo = (pos[0]-2, pos[1])
            enPassantCheckRight = (pos[0], pos[1]-1)
            enPassantCheckLeft = (pos[0], pos[1]+1)
             
        #going left
        elif self._direction == 4:
            posUp = (pos[0], pos[1]-1)
            posUpRight = (pos[0]+1, pos[1]-1)
            posUpLeft = (pos[0]-1, pos[1]-1)
            posUpTwo = (pos[0], pos[1]-2)
            enPassantCheckRight = (pos[0]+1, pos[1])
            enPassantCheckLeft = (pos[0]-1, pos[1])

        #normal moves
        if board.valid_square(posUp) and isinstance(board[posUp], EmptySquare):
                valid.append(posUp)

        if board.valid_square(posUpRight) and not isinstance(board[posUpRight], EmptySquare) and board[posUpRight].get_colour() not in self._team_colours:
                valid.append(posUpRight)

        if board.valid_square(posUpLeft) and not isinstance(board[posUpLeft], EmptySquare) and board[posUpLeft].get_colour() not in self._team_colours:
                valid.append(posUpLeft)

        if posUp in valid and not self._moved:
            if board.valid_square(posUpTwo) and isinstance(board[posUpTwo], EmptySquare):
                valid.append(posUpTwo)

        #en passant
        # first line is for 2 player, 2nd line does 4 player 
        if board.valid_square(enPassantCheckRight) and ((isinstance(board[enPassantCheckRight], Pawn) and board[enPassantCheckRight].get_enPassable == True and board[enPassantCheckRight].get_colour not in self._team_colours) \
                or (isinstance(board[posUp], Pawn) and board[posUp].get_enPassable == True and board[posUp].get_colour not in self._team_colours and (board[posUp]._direction == self._direction-1 or board[posUp]._direction == self._direction+3)) and isinstance(board[posUpRight], EmptySquare)):
            valid.append(posUpRight)
        if board.valid_square(enPassantCheckLeft) and ((isinstance(board[enPassantCheckLeft], Pawn) and board[enPassantCheckLeft].get_enPassable == True and board[enPassantCheckLeft].get_colour not in self._team_colours) \
                or (isinstance(board[posUp], Pawn) and board[posUp].get_enPassable == True and board[posUp].get_colour not in self._team_colours and (board[posUp]._direction == self._direction+1 or board[posUp]._direction == self._direction-3)) and isinstance(board[posUpLeft], EmptySquare)):
            valid.append(posUpLeft)
        return valid

#testing
if __name__ == "__main__":
    board = Board()
    board["G7"] = Pawn(3,'black',enPassable = False)
    board["A6"] = Pawn(1, "white",moved=True)
    board["B6"] = Pawn(3,'black',enPassable = True)
    board["A2"] = Pawn(1,"white",enPassable = False)
    board["G6"] = Pawn(4, "blue", enPassable = True)
    board["G4"] = Pawn(4, "blue", moved = False)
    board["B4"] = Pawn(2, "green", moved = False)

    print(board["A6"].valid_moves("A6", board))
    print(board["G7"].valid_moves("G7", board))
    print(board["A2"].valid_moves("A2", board))
    print(board["G4"].valid_moves("G4", board))
    print(board["B4"].valid_moves("B4", board))


