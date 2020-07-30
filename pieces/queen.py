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

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Board) -> List[str]:
        valid = []

        valid += Rook.valid_moves(self, position, board)
        valid += Bishop.valid_moves(self, position, board)

        return valid


if __name__ == "__main__":
    board = Board()

    board["A1"] = Queen("white")
    board["H1"] = Queen("white")

    board["A8"] = Queen("black")
    board["H8"] = Queen("black")

    print(board["A1"].valid_moves("A1", board))
