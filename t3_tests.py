import unittest
from t3_state import T3State
from t3_action import T3Action
from t3_player import choose


class TestT3Game(unittest.TestCase):
    def test_t3_state_transitions_t0(self):
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

    def test_t3_state_transitions_t1(self):
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

    # Add more test cases here as needed

    # Tests with small number of transitions
    # ---------------------------------------------------------------------------

    def test_t3_player_small_t0(self):
        state = [
            [6, 4, 1],
            [1, 1, 4],
            [4, 1, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(2, 2, 6), action)

    def test_t3_player_small_t1(self):
        state = [
            [6, 4, 1],
            [1, 1, 4],
            [4, 0, 0]
        ]
        t3state = T3State(True, state)
        action = choose(t3state)
        self.assertEqual(T3Action(2, 2, 1), action)

    def test_t3_player_small_t2(self):
        state = [
            [6, 4, 0],
            [1, 1, 4],
            [0, 0, 6]
        ]
        t3state = T3State(True, state)
        action = choose(t3state)
        self.assertEqual(None, action)

    def test_t3_player_small_t3(self):
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

    def test_t3_player_t0(self):
        state = [
            [2, 1, 0],
            [0, 0, 0],
            [0, 0, 6]
        ]
        t3state = T3State(True, state)
        action = choose(t3state)
        self.assertEqual(T3Action(1, 1, 5), action)

    def test_t3_player_t1(self):
        state = [
            [2, 1, 0],
            [0, 5, 0],
            [0, 0, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(2, 2, 6), action)

    def test_t3_player_t2(self):
        state = [
            [0, 1, 0],
            [0, 5, 0],
            [0, 0, 6]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 0, 2), action)

    def test_t3_player_t3(self):
        state = [
            [0, 0, 0],
            [0, 5, 0],
            [0, 0, 0]
        ]
        t3state = T3State(False, state)
        action = choose(t3state)
        self.assertEqual(T3Action(0, 0, 2), action)

    def test_t3_player_t4(self):
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
        self.assertEqual(T3Action(1, 0, 1), action)

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
        self.assertEqual(T3Action(1, 1, 5), action)

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
        self.assertEqual(T3Action(1, 0, 2), action)

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
        self.assertEqual(T3Action(1, 1, 5), action)


if __name__ == '__main__':
    unittest.main()
