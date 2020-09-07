from typing import Iterable
from uuid import UUID

from core.entities import poll as entities
from core.repositories import BaseReadOnlyRepository
from core.repositories import BaseRepository
from core.use_cases import BaseUseCase


class PollAddUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository):
        self.repo = repo

    def execute(self, other: entities.Question):
        with self.repo as repo:
            repo.add(other)


class PollGetUseCase(BaseUseCase):
    repo: BaseReadOnlyRepository

    def __init__(self, repo: BaseReadOnlyRepository):
        self.repo = repo

    def execute(self, question_id: UUID) -> entities.Question:
        return self.repo.get(question_id)


class PollListUseCase(BaseUseCase):
    repo: BaseReadOnlyRepository

    def __init__(self, repo: BaseReadOnlyRepository):
        self.repo = repo

    def execute(self) -> Iterable[entities.Question]:
        return self.repo.list()


class PollVoteUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository):
        self.repo = repo

    def execute(self, choice_id: UUID) -> entities.Choice:
        choice: entities.Choice = self.repo.get(choice_id)
        choice.vote()

        with self.repo as repo:
            repo.add(choice)
        return choice
