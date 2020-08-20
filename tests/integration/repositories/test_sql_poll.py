from pytest import fixture
from uuid import uuid4

from core.entities import poll as entity
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


def test_sql_repo_add(sql_session):
    repo = PollPSQLRepo(sql_session)

    uid = uuid4()

    q = entity.Question(
        id=uid,
        name='FAKE-NAME',
        text='FAKE-TEXT',
        choices=[
            entity.Choice(id=uuid4(), name='C1', text='T1'),
            entity.Choice(id=uuid4(), name='C2', text='T2'),
            entity.Choice(id=uuid4(), name='C3', text='T3'),
        ]
    )
    repo.save(q)
    print('### list', tuple(repo.list()))
    print('########### GET', repo.get(uid))
