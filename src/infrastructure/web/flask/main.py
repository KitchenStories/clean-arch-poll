from uuid import UUID

from flask import Flask
from flask import jsonify
from flask import request

from core.use_cases import poll as use_cases
from core.entities import poll as entity
from infrastructure.web import repo_instances

app = Flask(__name__)


@app.route('/polls', methods=['POST'])
def polls_add():
    post = request.form
    question: entity.Question = entity.Question(  # Need adapter for it
        id=UUID(post.get('id')),
        name=post.get('name'),
        text=post.get('text'),
    )
    uc = use_cases.PollAddUseCase(repo_instances.poll_repo)
    uc.execute(question)

    return jsonify(question)


@app.route('/polls', methods=['GET'])
def polls_list():
    uc = use_cases.PollListUseCase(repo_instances.poll_repo)
    questions = [q for q in uc.execute()]
    return jsonify(questions)


@app.route('/polls/<question_id>', methods=['GET'])
def polls_get(question_id):
    uc = use_cases.PollGetUseCase(repo_instances.poll_repo)
    question = uc.execute(question_id)
    return jsonify(question)


@app.route('/polls/vote/<choice_id>', methods=['POST'])
def choice_vote(choice_id):
    uc = use_cases.PollVoteUseCase(repo_instances.choice_repo)
    choice = uc.execute(choice_id)

    return jsonify(choice)
