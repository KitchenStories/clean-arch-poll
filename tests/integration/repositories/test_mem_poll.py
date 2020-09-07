from uuid import uuid4
from uuid import UUID

from infrastructure.repositories.mem import poll as repo


class TestPollMemRepo:
    def test_init_a(self, mocker, sent):
        q_id = uuid4()
        ch_id = uuid4()

        choice = {
            'id': ch_id,
            'name': sent.choice_name,
            'text': sent.choice_text,
            'votes': 99
        }
        question = {
            'id': str(q_id),
            'name': sent.name,
            'text': sent.text,
            'choices': [choice]
        }

        mocker.patch('infrastructure.repositories.mem.poll.repo_data.QUESTIONS', [question])
        mocker.patch('infrastructure.repositories.mem.poll.repo_data.CHOICES', [choice])
        m_question = mocker.patch(
            'infrastructure.repositories.mem.poll.entity.Question',
            return_value=sent.question
        )
        m_choice = mocker.patch(
            'infrastructure.repositories.mem.poll.entity.Choice',
            return_value=sent.choice
        )

        repo.PollMemRepo()

        exp_question = {
            'id': q_id,
            'name': sent.name,
            'text': sent.text,
            'choices': [sent.choice]
        }
        exp_choice = {
            'id': ch_id,
            'name': sent.choice_name,
            'text': sent.choice_text,
            'votes': 99
        }

        m_question.assert_called_once_with(
            id=UUID(question['id']),
            name=sent.name,
            text=sent.text,
            choices=[sent.choice]
        )
        m_question.assert_called_once_with(**exp_question)
        m_choice.assert_called_once_with(**exp_choice)

    def test_get(self, mocker, sent):
        uid = uuid4()
        mocker.patch(
            'infrastructure.repositories.mem.poll.repo_data.QUESTIONS', []
        )

        with repo.PollMemRepo() as rep:
            rep.data = {str(uid): sent.question}

            resp = rep.get(uid)

            assert resp == sent.question

    def test_list(self, mocker, sent):
        uid = uuid4()
        uid2 = uuid4()
        mocker.patch(
            'infrastructure.repositories.mem.poll.repo_data.QUESTIONS', []
        )

        with repo.PollMemRepo() as rep:
            rep.data = {str(uid): sent.question1, str(uid2): sent.question2}

            resp = rep.list()

            assert tuple(resp) == (sent.question1, sent.question2)

    def test_add(self, mocker):
        uid = uuid4()
        mocker.patch(
            'infrastructure.repositories.mem.poll.repo_data.QUESTIONS', []
        )

        with repo.PollMemRepo() as rep:
            rep.data = {}

            entity = mocker.Mock(id=uid, data={})
            rep.add(entity)

            assert rep.data == {}

        assert rep.data == {str(uid): entity}


class TestMemChoiceRepo:
    def test_init(self, mocker, sent):
        c_id = uuid4()
        m_choice = {'id': str(c_id)}
        mocker.patch(
            'infrastructure.repositories.mem.poll.repo_data.CHOICES', [m_choice]
        )
        m_choice_from_dict = mocker.patch(
            'infrastructure.repositories.mem.poll.entity.Choice.from_dict',
            return_value=sent.choice
        )

        repo.ChoiceMemRepo()
        m_choice_from_dict.assert_called_once_with(m_choice)

    def test_get(self, mocker, sent):
        uid = uuid4()
        mocker.patch('infrastructure.repositories.mem.poll.repo_data.CHOICES', [])

        with repo.ChoiceMemRepo() as rep:
            rep.data = {str(uid): sent.choice}
            resp = rep.get(uid)

            assert resp == sent.choice

    def test_list(self, mocker, sent):
        uid1 = uuid4()
        uid2 = uuid4()

        mocker.patch('infrastructure.repositories.mem.poll.repo_data.CHOICES', [])

        with repo.ChoiceMemRepo() as rep:
            rep.data = {str(uid1): sent.choice1, str(uid2): sent.choice2}

            resp = rep.list()

            assert tuple(resp) == (sent.choice1, sent.choice2)

    def test_add(self, mocker, sent):
        mocker.patch('infrastructure.repositories.mem.poll.repo_data.CHOICES', [])

        with repo.ChoiceMemRepo() as rep:
            choice = mocker.Mock(id=sent.id)
            rep.add(choice)
            assert rep.data == {}

        assert rep.data == {str(sent.id): choice}
