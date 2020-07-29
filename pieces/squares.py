from pieces.piece import Piece


class InvalidSquare(Piece):
    """
    InvalidSquare is a square where no pieces may exist.
    """
    def __init__(self):
        super().__init__("invalid", "x", 0, "")


class EmptySquare(Piece):
    """
    EmptySquare is a square where no pieces lie.
    """
    def __init__(self):
        super().__init__("empty", " ", 0, "")