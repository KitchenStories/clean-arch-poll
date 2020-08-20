from typing import List
from uuid import UUID

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.use_cases import poll as use_cases
from infrastructure.repositories.db import poll as db_repo
from infrastructure.repositories.db import Base
from infrastructure.repositories.mem import poll as mem_repo
from infrastructure.web.fastapi.adapters import poll as adapters

app = FastAPI()

# Mem
mem_choice_repo = mem_repo.ChoiceMemRepo()
mem_poll_repo = mem_repo.PollMemRepo(mem_choice_repo)

# SQLAlchemy
engine = create_engine('sqlite:///sqlite.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
db_choice_repo = db_repo.ChoicePSQLRepo(session)
db_poll_repo = db_repo.PollPSQLRepo(session)


@app.post("/polls", response_model=adapters.QuestionAdapter)
def add_question(question: adapters.QuestionAdapter) -> adapters.QuestionAdapter:
    uc = use_cases.PollAddUseCase(mem_poll_repo)
    uc.execute(question.to_entity())
    return question


@app.get("/polls/{question_id}", response_model=adapters.QuestionAdapter)
def get_poll(question_id: UUID) -> adapters.QuestionAdapter:
    uc = use_cases.PollGetUseCase(mem_poll_repo)
    question = uc.execute(question_id)
    return adapters.QuestionAdapter.from_entity(question)


@app.get("/polls", response_model=List[adapters.QuestionAdapter])
def list_polls() -> List[adapters.QuestionAdapter]:
    uc = use_cases.PollListUseCase(mem_poll_repo)
    questions = uc.execute()
    return [adapters.QuestionAdapter.from_entity(q) for q in questions]


@app.post('/polls/{vote_id}/vote', response_model=adapters.ChoiceAdapter)
def vote_choice(vote_id: UUID):
    uc = use_cases.PollVoteUseCase(mem_choice_repo)
    choice = uc.execute(vote_id)

    return adapters.ChoiceAdapter.from_entity(choice)
