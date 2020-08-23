import abc


class BaseUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, *args, **kwargs): ...  # pragma: no cover
