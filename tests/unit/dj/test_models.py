from uuid import uuid4

from core.entities import poll as entity
from infrastructure.web.dj.polls import models


class TestQuestion:
    def test_from_entity(self, sent):
        ent = entity.Question(id=uuid4(), name=sent.name, text=sent.text, choices=[])
        question = models.Question.from_entity(ent)

        assert isinstance(question, models.Question)
        assert question.id == ent.id
        assert question.name == ent.name
        assert question.text == ent.text

    def test_to_entity(self, mocker, sent):
        uid = uuid4()
        m_choice = mocker.Mock()
        m_choices = mocker.patch('infrastructure.web.dj.polls.models.Question.choices')
        m_choices.all.return_value = [m_choice]
        ent = models.Question(
            id=uid,
            name=sent.name,
            text=sent.text
        ).to_entity()

        assert isinstance(ent, entity.Question)
        assert ent.id == uid
        assert ent.name == sent.name
        assert ent.text == sent.text

        m_choices.all.assert_called_once_with()
        m_choice.to_entity.assert_called_once_with()


class TestChoice:
    def test_from_entity(self, sent):
        ent = entity.Choice(id=uuid4(), name=sent.name, text=sent.text, votes=sent.votes)
        choice = models.Choice.from_entity(ent)

        assert isinstance(choice, models.Choice)
        assert choice.id == ent.id
        assert choice.name == ent.name
        assert choice.text == ent.text
        assert choice.votes == ent.votes

    def test_to_entity(self, sent):
        uid = uuid4()
        ent = models.Choice(
            id=uid, name=sent.name, text=sent.text, votes=sent.votes
        ).to_entity()

        assert isinstance(ent, entity.Choice)
        assert ent.id == uid
        assert ent.name == sent.name
        assert ent.text == sent.text
        assert ent.votes == sent.votes

    def test_copy_from_entity(self, sent):
        uid = uuid4()
        ent = entity.Choice(id=uuid4(), name=sent.name, text=sent.text, votes=sent.votes)
        choice = models.Choice(id=uid, name='NAME', text='TEXT', votes=99)

        choice.copy_from_entity(ent)

        assert choice.id is not ent.id
        assert choice.name == ent.name
        assert choice.text == ent.text
        assert choice.votes == ent.votes
