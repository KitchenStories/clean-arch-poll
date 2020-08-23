from uuid import uuid4

from core.entities import poll as entities


class TestChoice:
    def test_from_dict(self, sent):
        c = entities.Choice.from_dict({
            'name': sent.name,
            'text': sent.text
        })

        assert isinstance(c, entities.Choice)
        assert c.name == sent.name
        assert c.text == sent.text

    def test_dict(self, sent):
        ch = entities.Choice(
            id=sent.id,
            name=sent.name,
            text=sent.text,
            votes=sent.votes
        )

        resp = ch.dict()

        assert resp == {
            'id': sent.id,
            'name': sent.name,
            'text': sent.text,
            'votes': sent.votes
        }

    def test_vote(self, sent):
        c = entities.Choice(
            id=uuid4(),
            name=sent.name,
            text=sent.text,
            votes=0
        )
        assert c.votes == 0
        c.vote()
        assert c.votes == 1


class TestQuestion:

    def test_from_dict(self, sent):
        q = entities.Question.from_dict({
            'name': sent.name,
            'text': sent.text,
            'choices': [{'name': sent.qname, 'text': sent.qtext}]
        })

        assert isinstance(q, entities.Question)
        assert q.name == sent.name
        assert q.text == sent.text

        choice = q.choices[0]
        assert isinstance(choice, entities.Choice)
        assert choice.name == sent.qname
        assert choice.text == sent.qtext

    def test_dict(self, mocker, sent):
        m_choice = mocker.Mock()
        m_choice.dict.return_value = sent.choice
        q = entities.Question(
            id=sent.id,
            name=sent.name,
            text=sent.text,
            choices=[m_choice],
        )

        resp = q.dict()

        assert resp == {
            'id': sent.id,
            'name': sent.name,
            'text': sent.text,
            'choices': [sent.choice]
        }

    def test_get_choice_by_id(self, mocker, sent):
        choice_id = uuid4()
        q = entities.Question(
            id=uuid4(),
            name=sent.name,
            text=sent.text,
            choices=[
                entities.Choice(
                    id=choice_id,
                    name=sent.choice_name,
                    text=sent.choice_text,
                    votes=1
                )
            ]
        )

        choice = q.get_choice_by_id(choice_id)
        assert choice.id == choice_id
