import os

from sqlmodel import create_engine, SQLModel, Session

from census.app.model.models import Model


# DATABASE_URL = os.environ.get("DATASOURCE_URL")
DATABASE_URL = "postgresql+pg8000://postgres:postgres@123/census"
print(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)
Model.metadata.create_all(engine)


def init_db():
    print("Connecting to db...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session