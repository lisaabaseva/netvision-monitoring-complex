import os

from sqlmodel import create_engine, SQLModel, Session

from model.models import Model
from config import Config

engine = create_engine(Config.DATABASE_URL, echo=True)
Model.metadata.create_all(engine)


def init_db():
    print("Connecting to db...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
