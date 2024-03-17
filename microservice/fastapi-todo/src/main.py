from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, create_engine, select, Session
from typing import Union, Optional, Annotated
from contextlib import asynccontextmanager

from src import settings


class TodoBase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str = Field(index=True)


connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)


#  Creates all tables associated with this metadata.
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# This is an asynchronous context manager that creates the tables when the FastAPI application starts.
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Hello World API with DB",
    version="0.0.1",
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Development Server",
        }
    ],
)


# This function is a context manager that yields a SQLAlchemy session. The session is used to interact with the database.
def get_session():
    with Session(engine) as session:
        yield session


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Create a new todo
@app.post("/todo", response_model=TodoBase)
def create_todo_api(todo: TodoBase, session: Session = Depends(get_session)):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo
