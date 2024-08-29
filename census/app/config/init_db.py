from sqlmodel import create_engine, SQLModel, Session

from model import BaseClass
from config import Config

config = Config()

engine = create_engine(config.DATABASE_URL, echo=True)
BaseClass.metadata.create_all(engine)


def init_db():
    print("Connecting to db...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
