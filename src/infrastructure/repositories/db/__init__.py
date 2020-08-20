import abc
import json

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta

from core.adapters import BaseAdapter
from core.entities import BaseEntity


class Base(declarative_base(BaseAdapter, metaclass=DeclarativeMeta)):
    __abstract__ = True

    def json(self) -> str:
        return json.dumps(self.dict())

    def dict(self) -> dict:
        return self.__dict__  # TODO: write correct func

    @abc.abstractmethod
    def copy_from_entity(self, other: BaseEntity): ...
