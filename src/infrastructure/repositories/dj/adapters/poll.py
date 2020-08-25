from dataclasses import dataclass
from typing import List
from uuid import UUID

from core.entities import poll as entity
from infrastructure.repositories.dj.adapters import DjangoAdapter
from infrastructure.web.dj.polls import models


@dataclass
class ChoiceAdapter(DjangoAdapter):
    id: UUID
    name: str
    text: str
    votes: int

    @classmethod
    def from_entity(cls, other: entity.Choice):
        return cls(
            id=other.id,
            name=other.name,
            text=other.text,
            votes=other.votes
        )

    @classmethod
    def from_model(cls, other: models.Choice):
        return cls(
            id=other.id,
            name=other.name,
            text=other.text,
            votes=other.votes
        )

    def to_entity(self):
        return entity.Choice(
            id=self.id,
            name=self.name,
            text=self.text,
            votes=self.votes
        )


@dataclass
class QuestionAdapter(DjangoAdapter):
    id: UUID
    name: str
    text: str
    choices: List[ChoiceAdapter]

    @classmethod
    def from_model(cls, other: models.Question):
        return cls(
            id=other.id,
            name=other.name,
            text=other.text,
            choices=[ChoiceAdapter.from_entity(ch) for ch in other.choices.all()]
        )

    @classmethod
    def from_entity(cls, other: entity.Question):
        return cls(
            id=other.id,
            name=other.name,
            text=other.text,
            choices=[ChoiceAdapter.from_entity(ch) for ch in other.choices]
        )

    def to_entity(self):
        return entity.Question(
            id=self.id,
            name=self.name,
            text=self.text,
            choices=[ch.to_entity() for ch in self.choices]
        )
