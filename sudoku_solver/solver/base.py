from abc import ABCMeta, abstractmethod


class BaseSolver():
    __metaclass__ = ABCMeta

    @abstractmethod
    def solve(self, state):
        """
        Get solution for given sudoku state.
        :param state:
        :return: None|State
        """
