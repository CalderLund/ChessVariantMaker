from piece import Piece
from typing import Tuple, Union, List
from board import Board
from squares import EmptySquare


class Rook(Piece):
    def __init__(self, colour: str, team_colours: List[str] = None):
        super().__init__("rook", "R", 5, colour, team_colours)

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Board) -> List[str]:
        valid = []

        # Get position in tuple format
        original_pos = Board.translate_pos(position)

        # Check up
        pos = original_pos
        while True:
            pos = (pos[0]+1, pos[1])
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            valid.append(pos)

        # Check down
        pos = original_pos
        while True:
            pos = (pos[0]-1, pos[1])
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            valid.append(pos)

        # Check right
        pos = original_pos
        while True:
            pos = (pos[0], pos[1]+1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            valid.append(pos)

        # Check left
        pos = original_pos
        while True:
            pos = (pos[0], pos[1]-1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            valid.append(pos)

        return valid


if __name__ == "__main__":
    board = Board()

    board["A1"] = Rook("white")
    board["H1"] = Rook("white")

    board["A8"] = Rook("black")
    board["H8"] = Rook("black")

    print(board["A1"].valid_moves("A1", board))
