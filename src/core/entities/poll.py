import uuid

from dataclasses import dataclass
from dataclasses import field

from typing import List

from core.entities import BaseEntity


@dataclass
class Choice(BaseEntity):
    name: str
    text: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
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
    name: str
    text: str
    choices: List[Choice] = field(default_factory=list)
    id: uuid.UUID = field(default_factory=uuid.uuid4)

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

    def get_choice_by_id(self, uid: uuid.UUID):
        choices = tuple(filter(lambda x: str(x.id) == str(uid), self.choices))
        return choices[0] if choices else None

    def dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'text': self.text,
            'choices': [ch.dict() for ch in self.choices],
        }
