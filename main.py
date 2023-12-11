import app.model
from app import app
from app.database import create_db_and_tables
from app.router import api_v1



# create_table()

app.include_router(api_v1, prefix='/v1')

@app.get("/test")
async def index():
    # await async_db.connect()
    create_db_and_tables()
    return "Hello world"