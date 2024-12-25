def noteEntity(item) -> dict:
    return {"_id": str(item["_id"]), "email": item["email"], "password": item["password"]}


def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]
