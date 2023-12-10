from databases import Database
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy


SERVER = 'localhost'
PORT = 5432
DB_USER = 'myuser'
DB_PASSWORD = '12345'
DB_NAME = 'mydb'

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{SERVER}:{PORT}/{DB_NAME}"

async_db = Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

Base = declarative_base()

def create_table():
    metadata.create_all(bind=engine)