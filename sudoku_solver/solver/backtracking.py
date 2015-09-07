from .base import BaseSolver


class BacktrackingSolver(BaseSolver):
    def __init__(self, rules):
        self.rules = rules

    def solve(self, state):
        try:
            self._solve(state)
        except SolutionFound as e:
            return e.get_solution()

    def _solve(self, state):
        pos = self._get_next_state_pos(state)

        if state.get_cell():
            new_state = state.clone()
            new_state.x, new_state.y = pos
            return self._solve(new_state)

        possible_values = self._get_possible_values(state)

        if not possible_values:
            return

        for value in possible_values:
            new_state = state.clone()
            new_state.set_cell(value)
            new_state.x, new_state.y = pos
            self._solve(new_state)

    def _get_next_state_pos(self, state):
        size = state.get_size()
        x, y = state.x, state.y

        if y < size - 1:
            y += 1
        elif x < size - 1:
            y = 0
            x += 1
        else:
            raise SolutionFound(state)

        return x, y

    def _get_possible_values(self, state):
        rules_possible_values = (set(r.get_possible_values(state)) for r in self.rules)
        possible_values = set.intersection(*rules_possible_values)
        return possible_values


class SolutionFound(Exception):
    def __init__(self, state, *args, **kwargs):
        super(SolutionFound, self).__init__(*args, **kwargs)
        self.solution = state

    def get_solution(self):
        return self.solution
