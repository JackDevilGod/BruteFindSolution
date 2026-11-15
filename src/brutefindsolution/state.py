from abc import ABC, abstractmethod
from typing import Self


class State(ABC):
    @abstractmethod
    def update(self) -> list[Self]:
        """
        updates the current state into all possible next states.

        Returns:
            list[State]: list of all possible next states.
        """

    @abstractmethod
    def at_goal(self) -> bool:
        """
        Test if the current state is the goal state.

        Returns:
            bool: returns true if this state is the goal, false otherwise
        """
