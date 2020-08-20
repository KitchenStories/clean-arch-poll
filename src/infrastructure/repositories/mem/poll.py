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
    def __init__(self, choice_repo: BaseRepository):
        self.choice_repo = choice_repo

        self.data = {
            q['id']: entity.Question(
                id=UUID(q.get('id')),
                name=q.get('name'),
                text=q.get('text'),
                choices=[
                    self.choice_repo.get(ch.get('id')) for ch in q.get('choices', [])
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
