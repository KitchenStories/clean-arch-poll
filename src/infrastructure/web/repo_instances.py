def get_mem_repo():
    from infrastructure.repositories.mem import poll as mem_repo

    mem_choice_repo = mem_repo.ChoiceMemRepo()
    mem_poll_repo = mem_repo.PollMemRepo(mem_choice_repo)
    return mem_choice_repo, mem_poll_repo


def get_sqlalchemy_repo():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    from infrastructure.repositories.db import Base
    from infrastructure.repositories.db import poll as db_repo

    engine = create_engine('sqlite:///sqlite.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    db_choice_repo = db_repo.ChoicePSQLRepo(session)
    db_poll_repo = db_repo.PollPSQLRepo(session)
    return db_choice_repo, db_poll_repo


def get_django_repo():
    from infrastructure.repositories.dj import poll as dj_repo

    dj_choice_repo = dj_repo.ChoiceDJRepo()
    dj_poll_repo = dj_repo.QuestionDJRepo()
    return dj_choice_repo, dj_poll_repo


choice_repo, poll_repo = get_sqlalchemy_repo()
