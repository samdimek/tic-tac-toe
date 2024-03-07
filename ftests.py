from t3_state import *
from t3_action import *
from t3_player import *
import unittest
import pytest

class T3GradingTests(unittest.TestCase):
    

    # T3State tests for transitions
    # ---------------------------------------------------------------------------
    def test_t3_state_transitions_t0(self) -> None:
        state = [
        [6, 4, 1],
        [1, 1, 4],
        [4, 1, 0]
        ]
        t3state = T3State(False, state)
        transitions = set(t3state.get_transitions())
        result = {
        (T3Action(2, 2, 2),
        T3State(True, [
        [6, 4, 1],
        [1, 1, 4],
        [4, 1, 2]
        ])),
        (T3Action(2, 2, 4),
        T3State(True, [
        [6, 4, 1],
        [1, 1, 4],
        [4, 1, 4]
        ])),
        (T3Action(2, 2, 6),
        T3State(True, [
        [6, 4, 1],
        [1, 1, 4],
        [4, 1, 6]
        ]))
        }
        self.assertEqual(result, transitions)
        
    def test_t3_state_transitions_t1(self) -> None:
        state = [
        [2, 1, 2],
        [1, 1, 0],
        [2, 0, 6]
        ]
        t3state = T3State(True, state)
        transitions = set(t3state.get_transitions())
        result = {
        (T3Action(2, 1, 1),
        T3State(False, [
        [2, 1, 2],
        [1, 1, 1],
        [2, 0, 6]
        ])),
        (T3Action(2, 1, 3),
        T3State(False, [
        [2, 1, 2],
        [1, 1, 3],
        [2, 0, 6]
        ])),
        (T3Action(2, 1, 5),
        T3State(False, [
        [2, 1, 2],
        [1, 1, 5],
        [2, 0, 6]
        ])),
        (T3Action(1, 2, 1),
        T3State(False, [
        [2, 1, 2],
        [1, 1, 0],
        [2, 1, 6]
        ])),
        (T3Action(1, 2, 3),
        T3State(False, [
        [2, 1, 2],
        [1, 1, 0],
        [2, 3, 6]
        ])),
        (T3Action(1, 2, 5),
        T3State(False, [
        [2, 1, 2],
        [1, 1, 0],
        [2, 5, 6]
        ]))
        }
        self.assertEqual(result, transitions)
        
    def test_t3_state_transitions_t2(self) -> None:
        state = [
        [0, 1, 0],
        [0, 1, 0],
        [2, 0, 6]
        ]
        t3state = T3State(True, state)
        transitions = set(t3state.get_transitions())
        self.assertEqual(15, len(transitions))
        
    # Tests with small number of transitions (good for just starting testing)
    # ---------------------------------------------------------------------------
    def test_t3_player_small_t0(self) -> None:
        state = [
        [6, 4, 1],
        [1, 1, 4],
        [4, 1, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(2, 2, 6), action)
        
    def test_t3_player_small_t1(self) -> None:
        state = [
        [6, 4, 1],
        [1, 1, 4],
        [4, 0, 0]
        ]
        t3state = T3State(True, state)
        action = choose(t3state)
        self.assertEqual(T3Action(1, 2, 1), action)
        # Terminal states should return None for the action
        
    def test_t3_player_small_t2(self) -> None:
        state = [
        [6, 4, 0],
        [1, 1, 4],
        [0, 0, 6]
        ]
        t3state = T3State(True, state)
        action = choose(t3state)
        self.assertEqual(None, action)
        
    # Terminal states should return None for the action
    def test_t3_player_small_t3(self) -> None:
        state = [
        [6, 4, 2],
        [1, 1, 4],
        [1, 2, 1]
        ]
        t3state = T3State(True, state)
        action = choose(t3state)
        self.assertEqual(None, action)
    # Larger tests with multiple open tiles
    # ---------------------------------------------------------------------------
    def test_t3_player_t0(self) -> None:
        state = [
        [2, 1, 0],
        [0, 0, 0],
        [0, 0, 6]
        ]
        t3state = T3State(True, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 1, 1), action)
    def test_t3_player_t1(self) -> None:
        state = [
        [2, 1, 0],
        [0, 5, 0],
        [0, 0, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 1, 2), action)
        
    def test_t3_player_t2(self) -> None:
        state = [
        [0, 1, 0],
        [0, 5, 0],
        [0, 0, 6]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 0, 2), action)
        
    def test_t3_player_t3(self) -> None:
        state = [
        [0, 0, 0],
        [0, 5, 0],
        [0, 0, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 0, 2), action)
    
    def test_t3_player_t4(self) -> None:
        state = [
        [3, 0, 0],
        [0, 4, 0],
        [0, 0, 1]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 1, 2), action)
# Depth-tricky Cases
# ---------------------------------------------------------------------------
# [!] VERY IMPORTANT TODO:
# Make your own test cases to make sure that the depth tiebreaking works as
# intended -- invent some edge cases to make sure that depth of terminal is
# being correctly minimized in your agent's decisions!

    def test_t3_player_depth_tricky_t0(self):
        # In this case, the AI has two possible moves that lead to the same
        # state with the same utility, but one move is deeper than the other.
        # The AI should choose the shallower move.
        state = [
            [1, 2, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 1, 2), action)

    def test_t3_player_depth_tricky_t1(self):
        # In this case, the AI has two possible moves, one of which leads to
        # a deeper terminal state but with a higher utility. The AI should
        # choose the move that leads to the shallower terminal state.
        state = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 1, 2), action)

    def test_t3_player_depth_tricky_t2(self):
        # In this case, the AI has two possible moves, both leading to terminal
        # states with different utilities but the same depth. The AI should choose
        # the move with the higher utility.
        state = [
            [1, 2, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 1, 2), action)

    def test_t3_player_depth_tricky_t3(self):
        # In this case, the AI has two possible moves, both leading to terminal
        # states with different utilities and depths. The AI should choose the
        # move with the higher utility and shallower depth.
        state = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 1, 2), action)


if __name__ == '__main__':
    unittest.main()