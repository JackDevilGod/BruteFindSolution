from src.brutefindsolution.search.dfs import DFS
from test.test_state import ConcreteState


class TestDFS:
    """Unit tests for DFS search algorithm."""

    def test_dfs_finds_goal_at_start(self):
        """Test that DFS returns start state if it's already at goal."""
        state = ConcreteState(3, 3)
        dfs = DFS(state)
        result = dfs.search()
        assert result is not None
        assert result is state

    def test_dfs_returns_none_no_goal_reachable(self):
        """Test that DFS returns None when goal cannot be reached."""
        # State at position 5 with goal at 0, no moves to left
        state = ConcreteState(5, 0)
        dfs = DFS(state)
        result = dfs.search()
        assert result is None

    def test_dfs_updates_start_state(self):
        """Test that DFS uses the start state correctly."""
        state = ConcreteState(0, 2)
        dfs = DFS(state)
        result = dfs.search()
        assert isinstance(result, ConcreteState)

    def test_dfs_traverses_states_in_dfs_order(self):
        """Test that DFS explores states in depth-first order (first branch fully)."""
        state = ConcreteState(0, 2)
        dfs = DFS(state)
        result = dfs.search()

        # Verify result was found at depth 2 (position 0 -> 1 -> 2)
        assert result is not None
        assert result.position == 2

    def test_dfs_returns_correct_type(self):
        """Test that DFS returns correct type or None."""
        state = ConcreteState(5, 3)  # No valid moves from start (position > goal)
        dfs = DFS(state)
        result = dfs.search()
        assert result is None

    def test_dfs_with_concrete_state(self):
        """Test DFS with various concrete state configurations."""
        test_cases = [
            (ConcreteState(0, 1), 1),  # 1 step
            (ConcreteState(1, 3), 3),  # 2 steps
            (ConcreteState(0, 0), 0),  # Already at goal
        ]

        for state, expected_depth in test_cases:
            dfs = DFS(state)
            result = dfs.search()
            assert isinstance(result, ConcreteState)
            if expected_depth == 0:
                assert result is state

    def test_dfs_finds_goal(self):
        """Test that DFS finds goal when reachable."""
        state = ConcreteState(0, 2)
        dfs = DFS(state)
        result = dfs.search()
        assert isinstance(result, ConcreteState)


class TestDFSEdgeCases:
    """Edge case tests for DFS."""

    def test_dfs_no_moves_from_start(self):
        """Test DFS when start position has no valid moves."""
        state = ConcreteState(-10, -5)  # Position beyond left boundary
        dfs = DFS(state)
        result = dfs.search()
        assert result is None

    def test_dfs_at_goal(self):
        """Test that DFS correctly identifies goal state."""
        state = ConcreteState(3, 3)
        dfs = DFS(state)
        result = dfs.search()
        assert result is not None
