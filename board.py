import numpy as np
from constants import Positions, MAX_HEIGHT, MAX_WIDTH
from indexing import ChessIndexing as Idx
from pieces.piece import Piece
from pieces.squares import InvalidSquare, EmptySquare
from typing import Tuple, Union, Any


class Board:
    def __init__(self, height: int = 8, width: int = 8, invalid_squares: Positions = None):
        """
        Creates a board of size height x width.

        :param height: 0 < int <= MAX_HEIGHT
        :param width: 0 < int <= MAX_WIDTH
        :param invalid_squares: list(str) or list((int, int))
        """

        assert 0 < height <= MAX_HEIGHT
        assert 0 < width <= MAX_WIDTH

        if invalid_squares is None:
            invalid_squares = []
        self.__height = height
        self.__width = width
        self.__board = np.empty((height, width), Piece)

        for i in range(height):
            for j in range(width):
                if (i, j) in invalid_squares:
                    self.__board[i, j] = InvalidSquare()
                else:
                    self.__board[i, j] = EmptySquare()

    def get_height(self):
        """
        Returns the board's height.

        :return: int
        """
        return self.__height

    def get_width(self):
        """
        Returns the board's width.

        :return: int
        """
        return self.__width

    @staticmethod
    def translate_pos(pos: Union[Tuple[int, int], str]) -> Tuple[int, int]:
        """
        Static method for converting an chess position to python indexes.

        :param pos: (int, int) or str
        :return: (int, int)
        """
        if isinstance(pos, str):
            i, j = Idx.chess_to_index(pos)
        elif isinstance(pos, tuple) and len(pos) == 2:
            i, j = pos[0], pos[1]
        else:
            raise TypeError("unknown type " + str(type(pos)) + " for key")

        assert 0 <= i < MAX_HEIGHT
        assert 0 <= j < MAX_WIDTH

        return i, j

    def __getitem__(self, pos: Union[Tuple[int, int], str]) -> Piece:
        """
        Returns the Piece at pos.

        board = Board(...)
        board.__getitem__("E5") === board["E5"] -> item at E5
        board.__getitem__((3, 2)) === board[3, 2] -> item at (3, 2)

        :param pos: (int, int) or str
        :return: Piece
        """
        i, j = Board.translate_pos(pos)
        return self.__board[i, j]

    def __setitem__(self, pos: Union[Tuple[int, int], str], piece: Piece):
        """
        Sets the Piece at pos.

        :param pos: (int, int) or str
        :param piece: Piece
        """
        i, j = Board.translate_pos(pos)
        if isinstance(piece, Piece):
            self.__board[i, j] = piece
        else:
            raise TypeError("value must be a Piece")
        
    def __str__(self) -> str:
        """
        Returns the string a board.

        :return: str
        """
        board = " " + "-" * (self.__width*2 + 1) + "\n"
        for i in range(self.__height-1, -1, -1):
            board += "| "
            for j in range(self.__width):
                piece = self.__board[i, j]
                if piece is None:
                    board += "  "
                else:
                    board += str(self.__board[i, j]) + " "
            board += "|\n"
        board += " " + "-" * (self.__width*2 + 1)
        return board

    def isinstance(self, pos: Union[Tuple[int, int], str], instance: Any) -> bool:
        """
        Checks if the Piece at pos is of instance instance.

        :param pos: (int, int) or str
        :param instance: any
        :return: bool
        """
        i, j = Board.translate_pos(pos)
        return isinstance(self.__board[i, j], instance)

    def valid_square(self, pos: Union[Tuple[int, int], str]) -> bool:
        """
        Checks if the square at pos is valid.

        :param pos: (int, int) or str
        :return: bool
        """
        try:
            return not self.isinstance(pos, InvalidSquare)
        except (IndexError, AssertionError):
            return False


if __name__ == "__main__":
    # 4 player board
    invalid = set([])
    for i in range(3):
        for j in range(3):
            invalid.add((i, j))
            invalid.add((i+11, j))
            invalid.add((i, j+11))
            invalid.add((i+11, j+11))
    four_player = Board(14, 14, invalid)

    assert str(four_player["A1"]) == "x"
    assert str(four_player[0, 0]) == "x"
    assert str(four_player["E5"]) == " "
    assert str(four_player) == \
        """ -----------------------------
| x x x                 x x x |
| x x x                 x x x |
| x x x                 x x x |
|                             |
|                             |
|                             |
|                             |
|                             |
|                             |
|                             |
|                             |
| x x x                 x x x |
| x x x                 x x x |
| x x x                 x x x |
 -----------------------------"""

    # classic board
    classic = Board(8, 8)
    assert str(classic) == \
        """ -----------------
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
 -----------------"""

    assert not classic.isinstance("A1", InvalidSquare)
    assert classic.isinstance("A1", EmptySquare)
    assert classic.isinstance("A1", Piece)

    classic["A1"] = InvalidSquare()

    assert classic.isinstance("A1", InvalidSquare)
    assert not classic.isinstance("A1", EmptySquare)
    assert classic.isinstance("A1", Piece)

    assert str(classic) == \
        """ -----------------
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
| x               |
 -----------------"""

    assert not classic.valid_square("A1")
    assert classic.valid_square("A8")
    assert classic.valid_square("H1")
    assert classic.valid_square("H8")
    assert classic.valid_square("B4")
    assert not classic.valid_square("I3")
    assert not classic.valid_square("C10")