from queue import LifoQueue as Queue

from src.brutefindsolution.search.abstract import Search
from src.brutefindsolution.state import State


class BFS(Search):
    def search(self) -> State | None:
        if self._start.at_goal():
            return self._start

        state_list: Queue[State] = Queue()
        state_list.put(self._start)

        while not state_list.empty():
            current_state = state_list.get()

            for next_state in current_state.update():
                if next_state.at_goal():
                    return next_state

                state_list.put(next_state)

        return None
