import app.model

from app import app
from app.router import api_v1
from app.core.database import create_db_and_tables


# create_table()
app.include_router(api_v1, prefix="/v1")


create_db_and_tables()

@app.get("/test")
def index():
    return "Hello world"
