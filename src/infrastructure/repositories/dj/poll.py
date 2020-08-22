from typing import Iterable
from uuid import UUID

from core.entities import poll as entity
from core.repositories import BaseRepository
from infrastructure.web.dj.adapters import poll as adapter
from infrastructure.web.dj.polls import models


class ChoiceDJRepo(BaseRepository):
    def get(self, uid: UUID) -> entity.Choice:
        choice = models.Choice.objects.get(id=uid)
        return adapter.ChoiceAdapter.from_model(choice).to_entity()

    def list(self) -> Iterable[entity.Choice]:
        return (
            adapter.ChoiceAdapter.from_model(choice).to_entity()
            for choice in models.Choice.objects.all()
        )

    def save(self, other: entity.Choice):
        try:  # update
            choice: models.Choice = models.Choice.objects.get(pk=other.id)
            choice.copy_from_entity(other)
        except models.Choice.DoesNotExist:  # create
            choice = models.Choice.from_entity(other)

        choice.save()

        return choice


class QuestionDJRepo(BaseRepository):
    def get(self, uid: UUID) -> entity.Question:
        question = models.Question.objects.get(id=uid)
        return adapter.QuestionAdapter.from_model(question).to_entity()

    def list(self) -> Iterable[entity.Question]:
        return (
            adapter.QuestionAdapter.from_model(question).to_entity()
            for question in models.Question.objects.all()
        )

    def save(self, other: entity.Question):
        try:  # update
            question: models.Choice = models.Question.objects.get(pk=other.id)
            question.copy_from_entity(other)
        except models.Question.DoesNotExist:  # create
            question = models.Question.from_entity(other)

        question.save()

        return question
