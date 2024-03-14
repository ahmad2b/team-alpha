# Todo functions
# 1. Create a todo
# 2. Get a todo
# 3. Update a todo
# 4. Delete a todo
# 5. Get all todos

from sqlmodel import SQLModel
from typing import Optional


# Todo model/structure/type
class Todo(SQLModel):
    id: Optional[int] = None
    title: str
    description: str


demo_todo = Todo(id=1, title="Demo Todo", description="This is a demo todo")

todo_db = [demo_todo]


def create_todo(todo: Todo):
    todo_db.append(todo)
    return todo


def get_todo_by_id(todo_id: int):
    for todo in todo_db:
        print("todo", todo)
        if todo.id == todo_id:
            return todo
    return None


def update_todo_by_id(todo_id: int, todo: Todo):
    for i in range(len(todo_db)):
        if todo_db[i].id == todo_id:
            todo_db[i] = todo
            return todo
    return None


def delete_todo_by_id(todo_id: int):
    for i in range(len(todo_db)):
        if todo_db[i].id == todo_id:
            todo_db.pop(i)
            return None
    return None


def get_all_todos():
    return todo_db
