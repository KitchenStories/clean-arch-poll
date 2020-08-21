from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.repositories.db import Base
from infrastructure.repositories.db import poll as db_repo
from infrastructure.repositories.mem import poll as mem_repo

# Memory
mem_choice_repo = mem_repo.ChoiceMemRepo()
mem_poll_repo = mem_repo.PollMemRepo(mem_choice_repo)

# SQLAlchemy
engine = create_engine('sqlite:///sqlite.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
db_choice_repo = db_repo.ChoicePSQLRepo(session)
db_poll_repo = db_repo.PollPSQLRepo(session)

choice_repo = mem_choice_repo
poll_repo = mem_poll_repo
