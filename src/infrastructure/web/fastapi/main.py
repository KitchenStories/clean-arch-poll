from fastapi import FastAPI

from infrastructure.web.fastapi.routes import poll

app = FastAPI()

app.include_router(poll.router, prefix='/polls', tags=['Poll'])
