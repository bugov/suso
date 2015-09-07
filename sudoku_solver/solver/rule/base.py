from abc import ABCMeta, abstractmethod


class BaseRule():
    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def is_valid(cls, state, cell):
        pass

    @classmethod
    @abstractmethod
    def get_possible_values(cls, state):
        pass
