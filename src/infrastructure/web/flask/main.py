from flask import Flask, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.use_cases import poll as use_cases
from infrastructure.repositories.db import poll as db_repo
from infrastructure.repositories.db import Base
from infrastructure.repositories.mem import poll as mem_repo

app = Flask(__name__)

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


@app.route('/polls')
def polls_list():
    uc = use_cases.PollListUseCase(mem_poll_repo)
    questions = [q for q in uc.execute()]
    return jsonify(questions)
