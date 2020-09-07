import abc

from typing import Iterable
from uuid import UUID

from core.entities import poll as entity
from core.repositories import BaseRepository
from infrastructure.repositories.mem import data as repo_data


class MemBaseRepository(BaseRepository, abc.ABC):
    def __init__(self):
        self.data = {}
        self.add_queue = []
        self.remove_queue = []

    def get(self, uid: UUID) -> entity.BaseEntity:
        return self.data.get(str(uid))

    def list(self) -> Iterable[entity.BaseEntity]:
        return self.data.values()

    def add(self, other: entity.BaseEntity):
        self.add_queue.append(other)

    def remove(self, other: entity.BaseEntity):
        self.remove_queue.append(other)

    def commit(self):
        for e in self.add_queue:
            self.data[str(e.id)] = e

        for e in self.remove_queue:
            try:
                del self.data[str(e.id)]
            except:
                pass


class ChoiceMemRepo(MemBaseRepository):
    def __init__(self):
        super().__init__()

        self.data = {
            str(c['id']): entity.Choice.from_dict(c)
            for c in repo_data.CHOICES
        }


class PollMemRepo(MemBaseRepository):
    def __init__(self):
        super().__init__()

        self.choices_lookup = {
            str(ch['id']): ch
            for ch in repo_data.CHOICES
        }

        self.data = {
            q['id']: entity.Question(
                id=UUID(q.get('id')),
                name=q.get('name'),
                text=q.get('text'),
                choices=[
                    entity.Choice(
                        id=choice_dict.get('id'),
                        name=choice_dict.get('name'),
                        text=choice_dict.get('text'),
                        votes=choice_dict.get('votes', 0),
                    )
                    for choice in q.get('choices', [])
                    if (choice_dict := self.choices_lookup.get(str(choice.get('id'))))
                ]
            )
            for q in repo_data.QUESTIONS
        }
