from .base import BaseRule


class StandardRule(BaseRule):
    @classmethod
    def is_valid(cls, state, cell):
        row = state.get_row(state.x)
        if cell in set([c for c in row]):
            return False

        col = state.get_col(state.y)
        if cell in set([c for c in col]):
            return False

        pos = state.get_segment_pos()
        seg = state.get_segment(*pos)
        if cell in set([c for c in seg]):
            return False

        return True

    @classmethod
    def get_possible_values(cls, state):
        possible = []

        for num in range(1, state.get_size() + 1):
            if cls.is_valid(state, num):
                possible.append(num)

        return possible
