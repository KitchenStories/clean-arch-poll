import abc


class BaseAdapter(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def from_entity(cls, entity: any): ...

    @abc.abstractmethod
    def to_entity(self): ...
