import os

from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("SERVER")
PORT = os.getenv("PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{SERVER}:{PORT}/{DB_NAME}"

async_engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(async_engine)


async def get_async_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()


# async_db = Database(DATABASE_URL) // Version of SQLAlchemy is not support with sqlModel

# SQLAlchemy setup using SQLModel
DATABASE_URL_SYNC = f"postgresql://{DB_USER}:{DB_PASSWORD}@{SERVER}:{PORT}/{DB_NAME}"       
sqlmodel_engine = create_engine(DATABASE_URL_SYNC, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(bind=sqlmodel_engine)
