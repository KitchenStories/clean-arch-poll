import abc

from typing import Iterable
from uuid import UUID

from core.entities import BaseEntity


class ContextManagerRepository(abc.ABC):
    @abc.abstractmethod
    def commit(self): ...  # pragma: no cover

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.commit()


class BaseReadOnlyRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, uid: UUID) -> BaseEntity: ...  # pragma: no cover

    @abc.abstractmethod
    def list(self) -> Iterable[BaseEntity]: ...  # pragma: no cover


class BaseWriteOnlyRepository(ContextManagerRepository):
    @abc.abstractmethod
    def add(self, other: BaseEntity): ...  # pragma: no cover

    @abc.abstractmethod
    def remove(self, other: BaseEntity): ...  # pragma: no cover


class BaseRepository(BaseReadOnlyRepository, BaseWriteOnlyRepository, abc.ABC):
    ...  # pragma: no cover
