"""
All logic concerning the T3 board state, including:
    1. the ability to get the transitions(which you must complete!)
    2. and available actions,
    3. and determine if the turn is for the odd / even player
"""

from dataclasses import dataclass
from typing import Optional, List, Tuple, Iterator
from t3_action import T3Action
import copy
import itertools

@dataclass
class T3State:
    MAX_MOVE = 6
    WIN_TARGET = 13
    DEFAULT_SIZE = 3

    def __init__(self, odd_turn: bool, state: Optional[List[List[int]]]):
        if state:
            self._state: List[List[int]] = state
        else:
            self._state = [[0] * T3State.DEFAULT_SIZE for x in range(T3State.DEFAULT_SIZE)]
        self._rows: int = len(self._state)
        self._cols: int = len(self._state[0])
        self._odd_turn: bool = odd_turn

    def is_valid_action(self, act: T3Action) -> bool:
        return act.col() >= 0 and act.col() < self._rows and \
               act.row() >= 0 and act.row() < self._cols and \
               act.move() >= 0 and act.move() <= T3State.MAX_MOVE and \
               (act.move() % 2 == 1 if self._odd_turn else act.move() % 2 == 0) and \
               self._state[act.row()][act.col()] == 0

    def get_next_state(self, act: Optional[T3Action]) -> "T3State":
        if act is None or not self.is_valid_action(act):
            raise ValueError("[X] Chosen action " + str(act) + " is invalid!")
        next_state = copy.deepcopy(self)
        next_state._state[act.row()][act.col()] = act.move()
        next_state._odd_turn = not next_state._odd_turn
        return next_state

    def get_open_tiles(self) -> List[Tuple[int, int]]:
        tile_pos = itertools.product(range(self._cols), range(self._rows))
        return [(c, r) for (c, r) in tile_pos if self._state[r][c] == 0]

    def get_moves(self) -> List[int]:
        return [move for move in range(1, T3State.MAX_MOVE + 1) if \
                (self._odd_turn and move % 2 == 1) or \
                (not self._odd_turn and move % 2 == 0)]

    def is_win(self) -> bool:
        rows = [sum([self._state[i][j] for i in range(self._rows)]) for j in range(self._cols)]
        cols = [sum([self._state[j][i] for i in range(self._cols)]) for j in range(self._rows)]
        diag1 = [sum([self._state[x][x] for x in range(self._rows)])]
        diag2 = [sum([self._state[x][self._cols - 1 - x] for x in range(self._rows)])]
        return T3State.WIN_TARGET in (rows + cols + diag1 + diag2)

    def is_tie(self) -> bool:
        return not self.is_win() and not self.get_open_tiles()

    def __str__(self) -> str:
        return "\n".join([str(r) for r in self._state])

    def __eq__(self, other: any) -> bool:
        if other is None: return False
        if not isinstance(other, T3State): return False
        return self._state == other._state and self._odd_turn == other._odd_turn

    def __hash__(self) -> int:
        return hash((str(self._state), self._odd_turn))

    def get_transitions(self) -> Iterator[Tuple[T3Action, "T3State"]]:
        for row, col in self.get_open_tiles():
            for move in self.get_moves():
                action = T3Action(row, col, move)
                yield action, self.get_next_state(action)
