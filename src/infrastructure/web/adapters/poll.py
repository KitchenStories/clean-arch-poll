from typing import List
from uuid import UUID

from core.entities import poll as entities
from infrastructure.web.adapters import PydanticAdapter


class ChoiceAdapter(PydanticAdapter):
    id: UUID
    name: str
    text: str
    votes: int = 0

    @classmethod
    def from_entity(cls, entity: entities.Choice):
        return cls(
            id=entity.id,
            name=entity.name,
            text=entity.text,
            votes=entity.votes
        )

    def to_entity(self):
        return entities.Choice(
            id=self.id,
            name=self.name,
            text=self.text,
            votes=self.votes
        )


class QuestionAdapter(PydanticAdapter):
    id: UUID
    name: str
    text: str
    choices: List[ChoiceAdapter]

    @classmethod
    def from_entity(cls, entity: entities.Question):
        return cls(
            id=entity.id,
            name=entity.name,
            text=entity.text,
            choices=[ChoiceAdapter.from_entity(ch) for ch in entity.choices]
        )

    def to_entity(self):
        return entities.Question(
            id=self.id,
            name=self.name,
            text=self.text,
            choices=[ch.to_entity() for ch in self.choices]
        )
