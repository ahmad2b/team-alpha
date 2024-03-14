from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI instance with the name app and the FastAPI class


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/todo")

@app.patch()

@app.delete()

@app.put()