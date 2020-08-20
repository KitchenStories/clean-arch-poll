from flask import Flask
from flask import jsonify

from core.use_cases import poll as use_cases
from infrastructure.web import repo_instances

app = Flask(__name__)


@app.route('/polls')
def polls_list():
    uc = use_cases.PollListUseCase(repo_instances.mem_poll_repo)
    questions = [q for q in uc.execute()]
    return jsonify(questions)
