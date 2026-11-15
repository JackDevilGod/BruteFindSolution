"""Integration tests for the search algorithms and state management."""

from src.brutefindsolution.search.bfs import BFS
from src.brutefindsolution.search.dfs import DFS
from test.test_state import ConcreteState


class TestBFSIntegration:
    """Integration tests testing BFS with concrete state implementation."""

    def test_bfs_integration_simple_maze(self):
        """Test BFS on a simple linear maze from 0 to 3."""
        start = ConcreteState(0, 3)
        bfs = BFS(start)
        result = bfs.search()

        assert result is not None
        assert result.position == 3

    def test_bfs_integration_longer_maze(self):
        """Test BFS on a longer linear maze from 0 to 5."""
        start = ConcreteState(0, 5)
        bfs = BFS(start)
        result = bfs.search()

        assert result is not None
        assert result.position == 5

    def test_bfs_integration_already_at_goal(self):
        """Test BFS when starting at goal state."""
        start = ConcreteState(2, 2)
        bfs = BFS(start)
        result = bfs.search()

        assert result is not None
        assert result is start


class TestDFSIntegration:
    """Integration tests testing DFS with concrete state implementation."""

    def test_dfs_integration_simple_maze(self):
        """Test DFS on a simple linear maze from 0 to 3."""
        start = ConcreteState(0, 3)
        dfs = DFS(start)
        result = dfs.search()

        assert result is not None
        assert result.position == 3

    def test_dfs_integration_already_at_goal(self):
        """Test DFS when starting at goal state."""
        start = ConcreteState(2, 2)
        dfs = DFS(start)
        result = dfs.search()

        assert result is not None
        assert result is start


class TestIntegrationWithEmptyStates:
    """Integration tests for edge cases with no valid moves."""

    def test_integration_no_moves_backwards(self):
        """Test that BFS returns None when goal is in invalid direction."""
        # Position 0 with goal at -1, can only move right but goal is left
        start = ConcreteState(0, -1)
        bfs = BFS(start)
        result = bfs.search()

        assert result is None

    def test_integration_no_moves_forwards(self):
        """Test that DFS returns None when goal is in invalid direction."""
        # Position 5 with goal at 6, can only move left but goal is right
        start = ConcreteState(5, 6)
        dfs = DFS(start)
        result = dfs.search()

        assert result is None

    def test_integration_both_algorithms_consistent(self):
        """Test that both BFS and DFS find the same goal."""
        start = ConcreteState(0, 2)

        bfs = BFS(start)
        dfs = DFS(start)

        result_bfs = bfs.search()
        result_dfs = dfs.search()

        assert result_bfs is not None
        assert result_dfs is not None
        # Both should find a path to the goal
        assert result_bfs.position == 2
        assert result_dfs.position == 2


class TestIntegrationReturnTypes:
    """Tests for integration return types."""

    def test_bfs_returns_state_or_none(self):
        """Test that BFS returns State or None correctly."""
        start = ConcreteState(0, 1)
        bfs = BFS(start)

        result = bfs.search()
        assert isinstance(result, (ConcreteState, type(None)))
        assert result is not None

    def test_dfs_returns_state_or_none(self):
        """Test that DFS returns State or None correctly."""
        start = ConcreteState(0, 1)
        dfs = DFS(start)

        result = dfs.search()
        assert isinstance(result, (ConcreteState, type(None)))
        assert result is not None
