from fastapi import FastAPI
from app.routes.user_routes import userdata
from app.routes.competition_routes import competition
from app.routes.entry_routes import entry

app = FastAPI()

app.include_router(userdata, tags=['users'])
app.include_router(competition, tags=['competition'])
app.include_router(entry, tags=['entry'])

@app.get("/")
def app_start():
    return {"start": "hello"}
