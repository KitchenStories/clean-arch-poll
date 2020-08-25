from typing import Iterable
from uuid import UUID

from core.entities import poll as entity
from core.repositories import BaseRepository
from infrastructure.repositories.mem import data as repo_data


class ChoiceMemRepo(BaseRepository):
    def __init__(self):
        self.data = {
            str(c['id']): entity.Choice.from_dict(c)
            for c in repo_data.CHOICES
        }

    def get(self, uid: UUID) -> entity.Choice:
        return self.data.get(str(uid))

    def list(self) -> Iterable[entity.Choice]:
        return self.data.values()

    def save(self, other: entity.Choice):
        self.data[str(other.id)] = other


class PollMemRepo(BaseRepository):
    def __init__(self):
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

    def get(self, uid: UUID) -> entity.Question:
        return self.data.get(str(uid))

    def list(self) -> Iterable[entity.Question]:
        return self.data.values()

    def save(self, other: entity.Question):
        self.data[str(other.id)] = other
