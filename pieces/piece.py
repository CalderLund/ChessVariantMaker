from typing import Tuple, Union, List, Any


class Piece:
    """
    Piece is a default superclass for all pieces to be built off of.
    """
    def __init__(self, name: str, symbol: str, value: int, colour: str, team_colours: List[str] = None):
        self._name = name
        self._symbol = symbol
        self._value = value
        self._colour = colour
        self.position = "--"

        if team_colours is None:
            self._team_colours = [colour]
        else:
            self._team_colours = team_colours
    
    def get_name(self) -> str:
        """
        Returns the name of the piece.
        """
        return self._name
    
    def get_symbol(self) -> str:
        """
        Returns the piece's board symbol. Alias for str(self).
        """
        return self._symbol
    
    def get_value(self) -> int:
        """
        Returns the over-the-board value of a piece.
        """
        return self._value
    
    def get_colour(self) -> str:
        """
        Returns the piece's colour.
        """
        return self._colour

    def valid_moves(self, board: Any) -> List[str]:
        """
        Returns an array of possible moves for the piece.
        eg. output ["E5", "F2", ...]
        """
        return []

    def in_check(self, ):

    def __str__(self) -> str:
        """
        Returns the string representation of a piece. Alias for self.get_symbol().
        """
        return self._symbol
