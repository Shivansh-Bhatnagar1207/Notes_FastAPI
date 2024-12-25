from pydantic import BaseModel


class Note(BaseModel):
    email : str
    password : str