from pytest import fixture

from infrastructure.repositories.db.models import Base
from infrastructure.repositories.db.poll import PollPSQLRepo
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


@fixture
def sql_session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def test_sql_repo_get_success(mocker, sent):
    m_db_question = mocker.Mock()
    m_db_question.to_entity.return_value = sent.en_question
    m_first_by_id = mocker.patch(
        'infrastructure.repositories.db.poll.PollPSQLRepo.first_by_id',
        return_value=m_db_question
    )

    repo = PollPSQLRepo(mocker.Mock())
    resp = repo.get(sent.uid)

    assert resp == sent.en_question
    m_first_by_id.assert_called_once_with(sent.uid)
    m_db_question.to_entity.assert_called_once_with()


def test_sql_repo_get_failed(mocker, sent):
    m_first_by_id = mocker.patch(
        'infrastructure.repositories.db.poll.PollPSQLRepo.first_by_id',
        return_value=None
    )

    repo = PollPSQLRepo(mocker.Mock())
    resp = repo.get(sent.uid)

    assert resp is None
    m_first_by_id.assert_called_once_with(sent.uid)


def test_sql_repo_add(mocker, sent):
    m_db_question_from_entity = mocker.patch(
        'infrastructure.repositories.db.poll.db.Question.from_entity',
        return_value=sent.db_question
    )
    m_session = mocker.Mock()
    with PollPSQLRepo(m_session) as repo:
        repo.add(sent.en_question)

        m_db_question_from_entity.assert_called_once_with(sent.en_question)
        m_session.add.assert_called_once_with(sent.db_question)
        m_session.commit.assert_not_called()

    m_session.commit.assert_called_once_with()
