from typing import List
from uuid import UUID
from fastapi import APIRouter

from core.use_cases import poll as use_cases
from infrastructure.web.fastapi.adapters import poll as adapters
from infrastructure.web import repo_instances

router = APIRouter()


@router.post("/", response_model=adapters.QuestionAdapter)
def add_question(question: adapters.QuestionAdapter) -> adapters.QuestionAdapter:
    uc = use_cases.PollAddUseCase(repo_instances.poll_repo)
    uc.execute(question.to_entity())
    return question


@router.get("/{question_id}", response_model=adapters.QuestionAdapter)
def get_poll(question_id: UUID) -> adapters.QuestionAdapter:
    uc = use_cases.PollGetUseCase(repo_instances.poll_repo)
    question = uc.execute(question_id)
    return adapters.QuestionAdapter.from_entity(question)


@router.get("/", response_model=List[adapters.QuestionAdapter])
def list_polls() -> List[adapters.QuestionAdapter]:
    uc = use_cases.PollListUseCase(repo_instances.poll_repo)
    questions = uc.execute()
    return [adapters.QuestionAdapter.from_entity(q) for q in questions]


@router.post('/vote/{choice_id}', response_model=adapters.ChoiceAdapter)
def vote_choice(choice_id: UUID):
    uc = use_cases.PollVoteUseCase(repo_instances.choice_repo)
    choice = uc.execute(choice_id)

    return adapters.ChoiceAdapter.from_entity(choice)
