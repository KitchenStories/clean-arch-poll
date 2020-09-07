from uuid import uuid4

from django.db import models

from core.entities import poll as entity


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    text = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    @classmethod
    def from_entity(cls, other: entity.Question):
        return cls(
            id=other.id,
            text=other.text,
            name=other.name
        )

    def to_entity(self) -> entity.Question:
        return entity.Question(
            id=self.id,
            name=self.name,
            text=self.text,
            choices=[ch.to_entity() for ch in self.choices.all()]
        )

    def copy_from_entity(self, other: entity.Question):
        self.name = other.name
        self.text = other.text


class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    @classmethod
    def from_entity(cls, other: entity.Choice):
        return cls(
            id=other.id,
            name=other.name,
            text=other.text,
            votes=other.votes
        )

    def to_entity(self) -> entity.Choice:
        return entity.Choice(
            id=self.id,
            name=self.name,
            text=self.text,
            votes=self.votes
        )

    def copy_from_entity(self, other: entity.Choice):
        self.name = other.name
        self.text = other.text
        self.votes = other.votes
