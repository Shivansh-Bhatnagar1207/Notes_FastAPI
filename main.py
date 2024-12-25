from fastapi import FastAPI
from routes.note import note
from fastapi.staticfffiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(note)
