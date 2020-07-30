from pieces.piece import Piece
from typing import Tuple, Union, List
from board import Board
from pieces.squares import EmptySquare
from copy import deepcopy


class King(Piece):
    """
    King is a Piece in chess.
    """
    def __init__(self, colour: str, team_colours: List[str] = None):
        super().__init__("king", "K", 20, colour, team_colours)

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Board) -> List[str]:
        valid = []
        position = Board.translate_pos(position)

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    pos = (position[0]+i, position[1]+j)
                    if board.valid_square(pos) and \
                            (isinstance(board[pos], EmptySquare) or board[pos].get_colour() not in self._team_colours):
                        temp = deepcopy(board)
                        temp[pos] = temp[position]
                        temp[position] = EmptySquare()
                        if not self.in_check(pos, temp):
                            valid.append(pos)

        return valid

    def in_check(self, position: Union[Tuple[int, int], str], board: Board) -> bool:
        """
        Returns if the King at position is in check.

        :param position: (int, int) or str
        :param board: Board
        :return: bool
        """
        position = Board.translate_pos(position)
        for i in range(board.get_height()):
            for j in range(board.get_width()):
                if (i != position[0] or j != position[1]) and \
                        board[i, j].get_colour() != self._colour and \
                        position in board[i, j].valid_moves((i, j), board):
                    return True
        return False


if __name__ == "__main__":
    board = Board()

    from pieces.queen import Queen

    board["E4"] = Queen("white")
    board["E5"] = King("white")

    board["D5"] = Queen("black")
    board["A1"] = Queen("black")

    assert board["E5"].in_check("E5", board)

    print(Board(invalid_squares = board["E4"].valid_moves("E4", board)))
    print(Board(invalid_squares = board["D5"].valid_moves("D5", board)))
    print(Board(invalid_squares = board["A1"].valid_moves("A1", board)))

    print(Board(invalid_squares = board["E5"].valid_moves("E5", board)))

