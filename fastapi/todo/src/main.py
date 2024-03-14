from typing import Union
from fastapi import FastAPI

from src.todofn import create_todo, get_todo_by_id, Todo, get_all_todos

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/todo/{item_id}")
def read_item(item_id: int):
    print("item_id", item_id)
    return get_todo_by_id(item_id)


@app.post("/todo")
def create_todo_api(title: str, description: str):
    _todo = Todo(id=2, title=title, description=description)
    todo = create_todo(_todo)
    return todo


@app.get("/todo")
def get_todos():
    return get_all_todos()
