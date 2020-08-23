import abc

from typing import Iterable
from uuid import UUID

from core.entities import BaseEntity


class BaseReadOnlyRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, uid: UUID) -> BaseEntity: ...  # pragma: no cover

    @abc.abstractmethod
    def list(self) -> Iterable[BaseEntity]: ...   # pragma: no cover


class BaseWriteOnlyRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self, other: BaseEntity): ...  # pragma: no cover


class BaseRepository(BaseReadOnlyRepository, BaseWriteOnlyRepository, metaclass=abc.ABCMeta):
    ...  # pragma: no cover
