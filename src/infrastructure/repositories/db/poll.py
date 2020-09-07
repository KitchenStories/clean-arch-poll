import abc

from typing import Iterable
from uuid import UUID

from sqlalchemy.orm import joinedload

from core.repositories import BaseRepository
from core.entities import poll as entity
from infrastructure.repositories.db import models as db


class BaseSQLRepo(BaseRepository, abc.ABC):
    def __init__(self, session):
        self.session = session

    def commit(self):
        self.session.commit()


class PollPSQLRepo(BaseSQLRepo):
    def first_by_id(self, uid: UUID, with_choices=True) -> db.Question:
        query = self.session.query(db.Question)
        if with_choices:
            query = query.options(
                joinedload(db.Question.choices)
            )
        query = query.filter(db.Question.id == str(uid))

        question: db.Question = query.first()
        return question

    def get(self, uid: UUID) -> entity.Question:
        choice = self.first_by_id(uid)
        return choice.to_entity() if choice else None

    def list(self) -> Iterable[entity.Question]:
        query = self.session.query(db.Question)
        query = query.options(
            joinedload(db.Question.choices)
        )

        return (question.to_entity() for question in query.all())

    def add(self, other: entity.Question):
        question = db.Question.from_entity(other)
        self.session.add(question)

    def remove(self, other: entity.Question):
        if question := self.first_by_id(other.id, with_choices=False):
            self.session.delete(question)


class ChoicePSQLRepo(BaseSQLRepo):
    def first_by_id(self, uid: UUID) -> db.Choice:
        query = self.session.query(db.Choice)
        query = query.filter(db.Choice.id == str(uid))
        choice = query.first()
        return choice

    def get(self, uid: UUID) -> entity.Choice:
        choice = self.first_by_id(uid)
        return choice.to_entity() if choice else None

    def list(self) -> Iterable[entity.Choice]:
        query = self.session.query(db.Choice)
        return (ch.to_entity() for ch in query.all())

    def add(self, other: entity.Choice):
        if choice := self.first_by_id(other.id):
            choice.copy_from_entity(other)
        else:
            choice = db.Choice.from_entity(other)

        self.session.add(choice)

    def remove(self, other: entity.Choice):
        if choice := self.first_by_id(other.id):
            choice.copy_from_entity(other)
            self.session.delete(choice)
