from pieces.piece import Piece
from typing import Tuple, Union, List
from board import Board
from pieces.squares import EmptySquare


class Rook(Piece):
    """
    Rook is a Piece in chess.
    """
    def __init__(self, colour: str, team_colours: List[str] = None):
        super().__init__("rook", "R", 5, colour, team_colours)

    def valid_moves(self, board: Board) -> List[str]:
        valid = []

        # Get position in tuple format
        original_pos = Board.translate_pos(self.position)

        # Check up
        pos = original_pos
        while True:
            pos = (pos[0]+1, pos[1])
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            if board.valid_square(pos) and \
                    not isinstance(board[pos], EmptySquare) and \
                    board[pos].get_colour() not in self._team_colours:
                valid.append(pos)
                break
            valid.append(pos)

        # Check down
        pos = original_pos
        while True:
            pos = (pos[0]-1, pos[1])
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            if board.valid_square(pos) and \
                    not isinstance(board[pos], EmptySquare) and \
                    board[pos].get_colour() not in self._team_colours:
                valid.append(pos)
                break
            valid.append(pos)

        # Check right
        pos = original_pos
        while True:
            pos = (pos[0], pos[1]+1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            if board.valid_square(pos) and \
                    not isinstance(board[pos], EmptySquare) and \
                    board[pos].get_colour() not in self._team_colours:
                valid.append(pos)
                break
            valid.append(pos)

        # Check left
        pos = original_pos
        while True:
            pos = (pos[0], pos[1]-1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            if board.valid_square(pos) and \
                    not isinstance(board[pos], EmptySquare) and \
                    board[pos].get_colour() not in self._team_colours:
                valid.append(pos)
                break
            valid.append(pos)

        return valid


if __name__ == "__main__":
    board = Board()

    board["A1"] = Rook("white")
    board["H1"] = Rook("white")

    board["A8"] = Rook("black")
    board["H8"] = Rook("black")

    print(Board(invalid_squares=board["A1"].valid_moves(board)))
