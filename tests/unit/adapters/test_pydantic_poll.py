from uuid import uuid4

from core.entities import poll as entity
from infrastructure.web.fastapi.adapters import poll as adapter


class TestChoiceAdapter:
    def test_from_entity(self):
        uid = uuid4()
        choice = entity.Choice(
            id=uid,
            name='FAKE-NAME',
            text='FAKE-TEXT',
            votes=9,
        )

        ad = adapter.ChoiceAdapter.from_entity(choice)

        assert isinstance(ad, adapter.ChoiceAdapter)
        assert choice.id == uid
        assert choice.name == 'FAKE-NAME'
        assert choice.text == 'FAKE-TEXT'
        assert choice.votes == 9

    def test_to_entity(self):
        uid = uuid4()
        ad = adapter.ChoiceAdapter(
            id=uid,
            name='FAKE-NAME',
            text='FAKE-TEXT',
            votes=9
        )

        en = ad.to_entity()
        assert isinstance(en, entity.Choice)
        assert en.id == uid
        assert en.name == 'FAKE-NAME'
        assert en.text == 'FAKE-TEXT'
        assert en.votes == 9


class TestQuestionAdapter:
    def test_from_entity(self):
        question = entity.Question(
            id=uuid4(),
            name='FAKE-NAME',
            text='FAKE-TEXT',
            choices=[]
        )

        ad = adapter.QuestionAdapter.from_entity(question)

        assert isinstance(ad, adapter.QuestionAdapter)
        assert ad.id == question.id
        assert ad.name == question.name
        assert ad.text == question.text

    def test_to_entity(self):
        uid = uuid4()
        en = adapter.QuestionAdapter(
            id=uid,
            name='FAKE-NAME',
            text='FAKE-TEXT',
            choices=[]
        ).to_entity()

        assert isinstance(en, entity.Question)
        assert en.id == uid
        assert en.name == 'FAKE-NAME'
        assert en.text == 'FAKE-TEXT'
