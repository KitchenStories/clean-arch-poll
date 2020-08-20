from uuid import uuid4

from core.entities import poll as entities


def test_choice_from_dict(sent):
    c = entities.Choice.from_dict({
        'name': sent.name,
        'text': sent.text
    })

    assert isinstance(c, entities.Choice)
    assert c.name == sent.name
    assert c.text == sent.text


def test_choice_vote(sent):
    c = entities.Choice(
        id=uuid4(),
        name=sent.name,
        text=sent.text,
        votes=0
    )
    assert c.votes == 0
    c.vote()
    assert c.votes == 1


def test_question_from_dict(sent):
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


def test_question_get_choice_by_id(mocker, sent):
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
