from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates("templates")


@note.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    docs = conn.comparesta.login.find({})
    newdocs = []
    for doc in docs:
        newdocs.append(
            {
                "id": doc["_id"],
                "email": doc["email"],
                "password": doc["password"],
            }
        )
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "newdocs": newdocs,
        },
    )


@note.post("/" )
async def create_item(request: Request):
    form = await request.form()
    formdict = dict(form)
    note =  conn.comparesta.login.insert_one(formdict)
    return {"DATA" : "Enetered successfully"}
