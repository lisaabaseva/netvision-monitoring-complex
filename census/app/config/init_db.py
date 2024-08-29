from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.engine import URL
import logging

from model import BaseClass
from config import Config

config = Config()

logger = logging.getLogger('census logs')
logger.warning(f'config.DATABASE_CONFIG.DRIVERNAME: {config.DATABASE_CONFIG.DRIVERNAME}')

url_object = URL.create(
    drivername=config.DATABASE_CONFIG.DRIVERNAME,
    port=config.DATABASE_CONFIG.DB_PORT,
    username=config.DATABASE_CONFIG.DB_USERNAME,
    password=config.DATABASE_CONFIG.DB_PASSWORD,
    host=config.DATABASE_CONFIG.DB_HOST,
    database=config.DATABASE_CONFIG.DB_NAME,
    query={'application_name': config.DATABASE_CONFIG.APPLICATION_NAME}
)
engine = create_engine(url_object, echo=True)
BaseClass.metadata.create_all(engine)


def init_db():
    print("Connecting to db...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
