from copy import deepcopy
from typing import Self

from src.brutefindsolution.state import State


class ConcreteState(State):
    """Concrete implementation of State for testing purposes."""

    def __init__(self, position: int, goal: int) -> None:
        self.position = position
        self.goal = goal

    def move(self, amount: int) -> None:
        self.position += amount

    def at_goal(self) -> bool:
        return self.position == self.goal

    def update(self) -> list[Self]:
        """Generate next states by moving left or right."""
        states = []
        next = deepcopy(self)
        if self.position > 0:
            next.move(-1)
        if self.position < self.goal:
            next.move(1)
        states.append(next)
        return states


def test_concrete_state_at_goal():
    """Test that at_goal returns True when position equals goal."""
    state = ConcreteState(3, 3)
    assert state.at_goal() is True

    state = ConcreteState(5, 3)
    assert state.at_goal() is False


def test_concrete_state_update_returns_empty_list():
    """Test that update returns empty list at goal."""
    state = ConcreteState(5, 5)
    assert len(state.update()) == 0


def test_concrete_state_update_with_goal_reachable():
    """Test that update returns valid next states when goal is reachable."""
    state = ConcreteState(3, 5)
    result = state.update()
    assert len(result) == 2
    for next_state in result:
        assert isinstance(next_state, ConcreteState)
        assert next_state.position in (2, 4)


def test_concrete_state_update_no_valid_moves():
    """Test update returns empty list when no valid moves exist."""
    # At start position with goal unreachable in this case
    state = ConcreteState(-10, -5)  # No move to the right since -10 < -5
    result = state.update()
    assert len(result) == 0


def test_concrete_state_update_multiple_moves():
    """Test that update returns all possible next states."""
    state = ConcreteState(2, 5)
    result = state.update()
    assert len(result) == 2
    # Should have moves to positions 1 and 3
    positions = [s.position for s in result]
    assert sorted(positions) == [1, 3]


def test_concrete_state_update_consistent_goal():
    """Test that all next states have the same goal."""
    state = ConcreteState(2, 5)
    result = state.update()
    for next_state in result:
        assert next_state.goal == 5
        assert next_state.at_goal() is False
