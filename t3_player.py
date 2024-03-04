from dataclasses import *
from typing import *
from t3_state import *


def choose(state: "T3State") -> Optional["T3Action"]:
    """
    Main workhorse of the Player that makes the optimal decision from the max node
    state given by the parameter to play the game of Tic-Tac-Total.
    [!] Remember the tie-breaking criteria! Moves should be selected in order of:
    1. Best utility
    2. Smallest depth of terminal
    3. Earliest move (i.e., lowest col, then row, then move number)
    You can view tiebreaking as something of an if-ladder: i.e., only continue to
    evaluate the depth if two candidates have the same utility, only continue to
    evaluate the earliest move if two candidates have the same utility and depth.
    Parameters:
    state (T3State):
    The board state from which the agent is making a choice. The board
    state will be either the odds or evens player's turn, and the agent
    should use the T3State methods to simplify its logic to work in
    either case.
    Returns:
    Optional[T3Action]:
    If the given state is a terminal (i.e., a win or tie), returns None.
    Otherwise, returns the best T3Action the current player could take
    from the given state by the criteria stated above.
    """
    return max_value(state, float('-inf'), float('inf'), 0)[1]


def max_value(state: "T3State", alpha: int, beta: int, depth: int) -> Tuple[int, Optional["T3Action"]]:
    if terminal_test(state):
        return utility(state), None

    best_val = float('-inf')
    best_action = None

    for action in possible_actions(state):
        next_state = result(state, action)
        min_val, _ = min_value(next_state, alpha, beta, depth + 1)
        if min_val > best_val:
            best_val = min_val
            best_action = action
        alpha = max(alpha, best_val)
        if beta <= alpha:
            break

    return best_val, best_action


def min_value(state: "T3State", alpha: int, beta: int, depth: int) -> Tuple[int, Optional["T3Action"]]:
    if terminal_test(state):
        return utility(state), None

    best_val = float('inf')
    best_action = None

    for action in possible_actions(state):
        next_state = result(state, action)
        max_val, _ = max_value(next_state, alpha, beta, depth + 1)
        if max_val < best_val:
            best_val = max_val
            best_action = action
        beta = min(beta, best_val)
        if beta <= alpha:
            break

    return best_val, best_action


def terminal_test(state: "T3State") -> bool:
    """
    Check if the given state is a terminal state (i.e., a win or a tie).

    Parameters:
    state (T3State): The current board state.

    Returns:
    bool: True if the state is terminal, False otherwise.
    """
    return state.is_win() or state.is_tie()


def possible_actions(state: "T3State") -> List["T3Action"]:
    """
    Return a list of possible actions from the given state.

    Parameters:
    state (T3State): The current board state.

    Returns:
    List[T3Action]: A list of possible actions.
    """
    actions = []
    for col, row in state.get_open_tiles():
        for move in state.get_moves():
            actions.append(T3Action(col, row, move))
    return actions


def result(state: "T3State", action: "T3Action") -> "T3State":
    """
    Apply the given action to the given state and return the resulting state.

    Parameters:
    state (T3State): The current board state.
    action (T3Action): The action to apply.

    Returns:
    T3State: The resulting board state after applying the action.
    """
    if not state.is_valid_action(action):
        raise ValueError("Invalid action: {}".format(action))

    next_state = copy.deepcopy(state)
    next_state._state[action.row()][action.col()] = action.move()
    next_state._odd_turn = not next_state._odd_turn
    return next_state

