# Simple class to specify actions to be made on the T3 board state, specifying a column, row, and number to place.
from dataclasses import dataclass
from typing import Any


@dataclass
class T3Action:
    """Class representing an action in the Tic-Tac-Toe variation game."""

    _col: int  # Column where the action is performed
    _row: int  # Row where the action is performed
    _move: int  # Number to place

    def col(self) -> int:
        """Get the column of the action."""
        return self._col

    def row(self) -> int:
        """Get the row of the action."""
        return self._row

    def move(self) -> int:
        """Get the number to place."""
        return self._move

    def __str__(self) -> str:
        """String representation of the action."""
        return "(" + str(self._col) + "," + str(self._row) + ") = " + str(self._move)

    def __lt__(self, other: "T3Action") -> bool:
        """Comparison method to compare actions."""
        col_diff = self._col - other._col
        row_diff = self._row - other._row
        mov_diff = self._move - other._move
        if not col_diff == 0:
            return col_diff < 0
        if not row_diff == 0:
            return row_diff < 0
        return mov_diff < 0

    def __eq__(self, other: any) -> bool:
        """Equality method to check if two actions are equal."""
        if other is None:
            return False
        if not isinstance(other, T3Action):
            return False
        return self._col == other._col and self._row == other._row and self._move == other._move

    def __hash__(self) -> int:
        """Hash method to calculate hash value of an action."""
        return hash((self._col, self._row, self._move))
