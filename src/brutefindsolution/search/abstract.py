from abc import ABC, abstractmethod

from src.brutefindsolution.state import State


class search(ABC):
    def __init__(self, start_state: State) -> None:
        """
        initialize the search with the state you want to start at.

        Args:
            start_state (State): starting state.
        """
        super().__init__()
        self._start = start_state

    @abstractmethod
    def search(self) -> State | None:
        """
        Call this to start the searching algorithm

        Returns:
            State | None: either returns the goal state, or None if the goal could not be reached.
        """
