from pieces.piece import Piece
from typing import Tuple, Union, List
from board import Board


class Pawn(Piece):
    def __init__(self, direction: int, colour: str, team_colours: List[str] = None, moved: bool = False):
        super().__init__("pawn", "P", 1, colour, team_colours)
        self._direction = direction
        self._moved = moved

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Board) -> List[str]:
        # GENERAL IDEA
        # take in position
        # generate possible moves outwards from position until invalid
        # create a list of possible moves as you check them
        # return the moves

        # TO CONSIDER
        # Queening (Probably handled by board)
        # En-passant
        # captures
        # first move

        """ EXAMPLE USE
        if board.valid_square((3, 2)):
            if board[3, 2].get_colour() != self._colour:
                #mark as valid
                True
            else:
                # mark as invalid
                False"""


if __name__ == "__main__":
    pawn = Pawn(1, "black")

    print(pawn) # "P"
