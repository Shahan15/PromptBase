from fastapi import FastAPI
from datetime import datetime
from routes import (users_router)


app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "Working"}


users = [
    {
        "id": 1,
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@doe.com",
        "password": "john1234",
        "dateCreated": datetime.now()
    },
    {
        "id": 2,
        "firstName": "John",
        "lastName": "Lark",
        "email": "john@dolarke.com",
        "password": "john1234",
        "dateCreated": datetime.now()
    }
]

app.include_router(users_router, tags=["Users"])
