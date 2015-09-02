from abc import ABCMeta, abstractmethod


class BaseFormat():
    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def to_data(cls, obj):
        pass

    @classmethod
    @abstractmethod
    def to_python(cls, data):
        pass
