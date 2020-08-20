import abc

from pydantic import BaseModel

from core.adapters import BaseAdapter


class PydanticAdapter(BaseModel, BaseAdapter, metaclass=abc.ABCMeta): ...  # noqa
