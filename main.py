# import app.model
from app import app
from app.database import async_db, create_table


# create_table()

@app.get("/")
async def index():
    # await async_db.connect()
    return "Hello world"    