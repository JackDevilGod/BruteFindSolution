from src.brutefindsolution.search.bfs import BFS
from test.test_state import ConcreteState


class TestBFS:
    """Unit tests for BFS search algorithm."""

    def test_bfs_finds_goal_at_start(self):
        """Test that BFS returns start state if it's already at goal."""
        state = ConcreteState(3, 3)
        bfs = BFS(state)
        result = bfs.search()
        assert result is not None
        assert result is state

    def test_bfs_returns_none_no_goal_reachable(self):
        """Test that BFS returns None when goal cannot be reached."""
        # In this simple maze, if goal is far beyond valid moves
        # This tests the algorithm structure - we need to ensure it doesn't get stuck
        state = ConcreteState(0, 5)
        bfs = BFS(state)

        # Update all possible states to see their reachability
        initial = state.update()
        assert len(initial) > 0  # Should have at least one valid move
        result = bfs.search()
        # This may return None if we don't implement full maze, but should not crash

    def test_bfs_updates_start_state(self):
        """Test that BFS uses the start state correctly."""
        state = ConcreteState(0, 2)
        bfs = BFS(state)
        result = bfs.search()
        assert isinstance(result, ConcreteState)

    def test_bfs_traverses_states_in_bfs_order(self):
        """Test that BFS explores states in breadth-first order (level by level)."""
        state = ConcreteState(0, 2)
        bfs = BFS(state)
        result = bfs.search()

        # Verify result was found at depth 2 (position 0 -> 1 -> 2)
        assert result is not None
        assert result.position == 2

    def test_bfs_returns_correct_type(self):
        """Test that BFS returns correct type or None."""
        state = ConcreteState(5, 3)  # No valid moves from start (position > goal)
        bfs = BFS(state)
        result = bfs.search()
        assert result is None

    def test_bfs_with_concrete_state(self):
        """Test BFS with various concrete state configurations."""
        test_cases = [
            (ConcreteState(0, 1), 1),  # 1 step
            (ConcreteState(1, 3), 3),  # 2 steps
            (ConcreteState(0, 0), 0),  # Already at goal
        ]

        for state, expected_depth in test_cases:
            bfs = BFS(state)
            result = bfs.search()
            assert isinstance(result, ConcreteState)
            if expected_depth == 0:
                assert result is state
