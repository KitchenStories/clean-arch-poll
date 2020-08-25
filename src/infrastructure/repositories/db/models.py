from uuid import UUID

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from core.entities import poll as entity
from infrastructure.repositories.db import Base


class Question(Base):
    __tablename__ = 'question'
    id = Column(String(50), primary_key=True)
    name = Column(String(50))
    text = Column(String(50))
    choices = relationship('Choice', back_populates='question')

    @classmethod
    def from_entity(cls, other: entity.Question):
        return cls(
            id=str(other.id),
            name=other.name,
            text=other.text,
            choices=[Choice.from_entity(ch) for ch in other.choices]
        )

    def to_entity(self) -> entity.Question:
        return entity.Question(
            id=UUID(self.id),
            name=self.name,
            text=self.text,
            choices=[ch.to_entity() for ch in self.choices]
        )

    def copy_from_entity(self, other: entity.Question):
        self.name = other.name
        self.text = other.text
        # self.choices = [ other.choices]


class Choice(Base):
    __tablename__ = 'choice'
    id = Column(String(50), primary_key=True)
    name = Column(String(50))
    text = Column(String(50))
    votes = Column(Integer)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship('Question', back_populates='choices')

    @classmethod
    def from_entity(cls, other: entity.Choice):
        return cls(
            id=str(other.id),
            name=other.name,
            text=other.text,
            votes=other.votes,
        )

    def to_entity(self) -> entity.Choice:
        return entity.Choice(
            id=UUID(self.id),
            name=self.name,
            text=self.text,
            votes=self.votes,
        )

    def copy_from_entity(self, other: entity.Choice):
        self.name = other.name
        self.text = other.text
        self.votes = other.votes
