from pieces.piece import Piece
from typing import Tuple, Union, List
from board import Board

from pieces.rook import Rook
from pieces.bishop import Bishop


class Queen(Piece):
    """
    Queen is a Piece in chess.
    """
    def __init__(self, colour: str, team_colours: List[str] = None):
        super().__init__("queen", "Q", 9, colour, team_colours)

    def valid_moves(self, board: Board) -> List[str]:
        valid = []

        valid += Rook.valid_moves(self, board)
        valid += Bishop.valid_moves(self, board)

        return valid


if __name__ == "__main__":
    board = Board()

    q = Queen("W")
    board["B2"] = q
    board["H2"] = Queen("W")

    board["B7"] = Queen("B")
    board["H8"] = Queen("B")

    print(board.__str__(colours=True))

    print(Board(invalid_squares=q.valid_moves(board)))
