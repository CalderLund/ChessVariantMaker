import re
from constants import ALPHA_LEN
from typing import Tuple


class ChessIndexing:
    """
    ChessIndexing is a helper class that contains two static methods:
    1. index_to_chess: converts a tuple of python indexes to a chess style index.
    2. chess_to_index: converts a chess style index to a tuple of python indexes.
    """
    @staticmethod
    def index_to_chess(i: int, j: int) -> str:
        """
        Ex.
        (2, 1)   --> "B3"
        (6, 3)   --> "D7"
        (10, 26) --> "AA11"
        """
        number = i + 1

        if 0 <= j < ALPHA_LEN:
            letter = chr(j + ord('A'))
            return str(letter) + str(number)
        
        for i in range(ALPHA_LEN):
            if ALPHA_LEN * (i + 1) <= j < ALPHA_LEN * (i + 2):
                letter = chr(i + ord('A')) + chr(j % ALPHA_LEN + ord('A'))
                return str(letter) + str(number)
        
        raise IndexError("indexes out of range")

    @staticmethod
    def chess_to_index(pos: str) -> Tuple[int, int]:
        """
        Ex.
        "B3"   --> (2, 1)
        "D7"   --> (6, 3)
        "AA11" --> (10, 26)
        """
        positions = re.findall(r"[A-Z][A-Z]?[1-9][0-9]*", pos)
        
        if len(positions) != 1:
            raise SyntaxError("must have uppercase letters followed by numbers")

        letter = re.findall(r"[A-Z][A-Z]?", positions[0])[0]
        number = re.findall(r"[1-9][0-9]*", positions[0])[0]

        if len(letter) == 2:
            j = ALPHA_LEN * (ord(letter[0]) - ord('A') + 1) + ord(letter[1]) - ord('A')
        else:
            j = ord(letter[0]) - ord('A')
        
        i = int(number) - 1

        return (i, j)


if __name__ == "__main__":
    expected = [
        (ChessIndexing.index_to_chess(2, 1), "B3"),
        (ChessIndexing.index_to_chess(6, 3), "D7"),
        (ChessIndexing.index_to_chess(10, 26), "AA11"),

        (ChessIndexing.chess_to_index("B3"), (2, 1)),
        (ChessIndexing.chess_to_index("D7"), (6, 3)),
        (ChessIndexing.chess_to_index("AA11"), (10, 26))
    ]
    for inp, out in expected:
        if inp != out:
            print(inp, "!=", out)
