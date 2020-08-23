import abc
from dataclasses import dataclass


@dataclass
class BaseEntity(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def from_dict(cls, other: dict): ...  # pragma: no cover

    @abc.abstractmethod
    def dict(self): ...  # pragma: no cover
