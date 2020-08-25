import abc

from core.adapters import BaseAdapter


class DjangoAdapter(BaseAdapter, metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def from_model(cls, other): ...
