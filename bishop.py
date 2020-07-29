from piece import Piece
from typing import Tuple, Union, List
from board import Board
from squares import EmptySquare


class Bishop(Piece):
    def __init__(self, colour: str, team_colours: List[str] = None):
        super().__init__("bishop", "B", 3, colour, team_colours)

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Board) -> List[str]:
        valid = []

        # Get position in tuple format
        original_pos = Board.translate_pos(position)

        # Check up/right
        pos = original_pos
        while True:
            pos = (pos[0]+1, pos[1]+1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            valid.append(pos)

        # Check down/right
        pos = original_pos
        while True:
            pos = (pos[0]-1, pos[1]+1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            valid.append(pos)

        # Check up/left
        pos = original_pos
        while True:
            pos = (pos[0]+1, pos[1]-1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
                break
            valid.append(pos)

        # Check down/left
        pos = original_pos
        while True:
            pos = (pos[0]-1, pos[1]-1)
            if not board.valid_square(pos) or \
                    (not isinstance(board[pos], EmptySquare) and board[pos].get_colour() in self._team_colours):
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

    print(board["A1"].valid_moves("A1", board))
