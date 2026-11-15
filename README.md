# BruteFindSolution

A simple search framework implementing Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms on abstract state spaces.

## Project Structure

```
src/
├── brutefindsolution/
│   ├── state.py              # Abstract base class `State`
│   ├── search/
│   │   ├── abstract.py       # Abstract base class `Search`
│   │   ├── bfs.py            # BFS search implementation
│   │   ├── dfs.py            # DFS search implementation
│   │   └── __init__.py       # Package init
└── test/
    ├── test_state.py         # Unit tests for `State`
    ├── test_bfs.py           # Unit tests for BFS
    ├── test_dfs.py           # Unit tests for DFS
    └── test_integration.py   # Integration tests
```

## Core Concepts

### `State` (abstract)
Represents a node in the search space. Must implement:
- `at_goal() -> bool`: Returns `True` if this state is the goal state
- `update() -> list[State]`: Returns all possible next states from the current state

### `Search` (abstract)
Base class for search algorithms. Takes a start state in its constructor and provides:
- `search() -> State | None`: Executes the search and returns the goal state if found, otherwise `None`

### BFS (Breadth-First Search)
Explores states level by level (breadth-first). Uses a queue (`queue.Queue`) for state traversal.

### DFS (Depth-First Search)
Explores states depth-first (follows first branch to completion). Uses a LIFO queue (`queue.LifoQueue`) for state traversal.

## Usage

```python
# Import concrete classes
from src.brutefindsolution.state import ConcreteState  # Provided for testing
from src.brutefindsolution.search.bfs import BFS
from src.brutefindsolution.search.dfs import DFS

# Create a start state (must implement State interface)
start = ConcreteState(0, 5)  # position=0, goal=5

# Use BFS
bfs = BFS(start)
goal_state = bfs.search()

# Use DFS  
dfs = DFS(start)
goal_state = dfs.search()
```

## Running Tests

Unit and integration tests can be run with Python's standard unittest module:

```bash
# From the project root:
python -m unittest discover test/
# or
python test/__main__.py  # if test files have a __main__
```

Or if pytest is installed:

```bash
pytest test/ -v
```

## Design Notes

- All search algorithms follow the same pattern: check if start is goal first, then traverse using a queue
- `State` is abstract and requires concrete implementations (e.g., `ConcreteState` in tests)
- `Search` is abstract and requires implementations (BFS and DFS provide them)
- Both BFS and DFS have identical search logic in their current implementation (same pseudocode), but differ in queue type (`Queue` vs `LifoQueue`)
- Tests validate:
  - Correct goal detection
  - Proper state update behavior
  - Algorithm correctness for reachable goals
  - Edge cases (no valid moves, already at goal)
  - Integration between state and algorithms

## Future Extensions

- Add more concrete state implementations (maze solver, graph search, etc.)
- Add heuristic search (A*, etc.)
- Improve state representation with better goal detection
- Add performance benchmarks
- Add CLI interface for interactive use
