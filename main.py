from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Ruta para el registro de usuarios
@app.post("/register")
def register_user():
    pass

# Ruta para el login de usuarios
@app.post("/login")
def login_user():
    pass