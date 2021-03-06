from pieces.piece import Piece
from typing import Tuple, Union, List
from board import Board
from pieces.squares import EmptySquare


class Bishop(Piece):
    """
    Bishop is a Piece in chess.
    """
    def __init__(self, colour: str, team_colours: List[str] = None):
        super().__init__("bishop", "B", 3, colour, team_colours)

    def valid_moves(self, board: Board) -> List[str]:
        valid = []

        # Get position in tuple format
        original_pos = Board.translate_pos(self.position)

        # Check up/right
        pos = original_pos
        while True:
            pos = (pos[0]+1, pos[1]+1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            if board.valid_square(pos) and \
                    not isinstance(board[pos], EmptySquare) and \
                    board[pos].get_colour() not in self._team_colours:
                valid.append(pos)
                break
            valid.append(pos)

        # Check down/right
        pos = original_pos
        while True:
            pos = (pos[0]-1, pos[1]+1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            if board.valid_square(pos) and \
                    not isinstance(board[pos], EmptySquare) and \
                    board[pos].get_colour() not in self._team_colours:
                valid.append(pos)
                break
            valid.append(pos)

        # Check up/left
        pos = original_pos
        while True:
            pos = (pos[0]+1, pos[1]-1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            if board.valid_square(pos) and \
                    not isinstance(board[pos], EmptySquare) and \
                    board[pos].get_colour() not in self._team_colours:
                valid.append(pos)
                break
            valid.append(pos)

        # Check down/left
        pos = original_pos
        while True:
            pos = (pos[0]-1, pos[1]-1)
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

    board["A1"] = Bishop("white")
    board["H1"] = Bishop("white")
    board["C3"] = Bishop("white")

    board["A8"] = Bishop("black")
    board["H8"] = Bishop("black")

    print(board["A1"].valid_moves(board))
    print(board["H1"].valid_moves(board))
