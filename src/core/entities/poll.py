from dataclasses import dataclass

from typing import List
from uuid import UUID

from core.entities import BaseEntity


@dataclass
class Choice(BaseEntity):
    id: UUID
    name: str
    text: str
    votes: int = 0

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get('id'),
            name=other.get('name'),
            text=other.get('text'),
            votes=other.get('votes', 0)
        )

    def dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'text': self.text,
            'votes': self.votes,
        }

    def vote(self):
        self.votes += 1


@dataclass
class Question(BaseEntity):
    id: UUID
    name: str
    text: str
    choices: List[Choice]

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get('id'),
            name=other.get('name'),
            text=other.get('text'),
            choices=[
                Choice.from_dict(ch)
                for ch in other.get('choices', ())
                if ch
            ]
        )

    def get_choice_by_id(self, uid: UUID):
        choices = tuple(filter(lambda x: str(x.id) == str(uid), self.choices))
        return choices[0] if choices else None

    def dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'text': self.text,
            'choices': [ch.dict() for ch in self.choices],
        }
