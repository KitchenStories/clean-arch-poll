import abc

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta

from core.adapters import BaseAdapter
from core.entities import BaseEntity


class Base(declarative_base(BaseAdapter, metaclass=DeclarativeMeta)):
    __abstract__ = True

    @abc.abstractmethod
    def copy_from_entity(self, other: BaseEntity): ...  # pragma: no cover
