from typing import Tuple, Union, List, Any


class Piece:
    """
    Piece is a default superclass for all pieces to be built off of.
    """
    def __init__(self, name: str, symbol: str, value: int, colour: str):
        """
        Initialize superclass Piece.

        :param name: str
        :param symbol: str
        :param value: int
        :param colour: str
        """
        self._name = name
        self._symbol = symbol
        self._value = value
        self._colour = colour
    
    def get_name(self) -> str:
        """
        Returns the name of the piece.

        :return: str
        """
        return self._name
    
    def get_symbol(self) -> str:
        """
        Returns the piece's board symbol. Alias for str(self).

        :return: str
        """
        return self._symbol
    
    def get_value(self) -> int:
        """
        Returns the over-the-board value of a piece.

        :return: int
        """
        return self._value
    
    def get_colour(self) -> str:
        """
        Returns the piece's colour.

        :return: str
        """
        return self._colour

    def valid_moves(self, position: Union[Tuple[int, int], str], board: Any) -> List[str]:
        """
        Returns an array of possible moves for the piece.

        :param position: (int, int) or str
        :param board: Board
        :return: [str, ...]

        eg output ["E5", "F2", ...]
        """
        pass

    def __str__(self) -> str:
        """
        Returns the string representation of a piece. Alias for self.get_symbol().

        :return: str
        """
        return self._symbol
