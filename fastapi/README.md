1. run the followig command to create a new project with poetry

```bash
poetry new helloworld --name src
```

2. Install FastAPI and Uvicorn

```bash
poetry add fastapi uvicorn[standard]
```

3. Create a new file in the `helloworld/src` directory called `main.py` and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

4. Run the server with the following command:

```bash
poetry run uvicorn src.main:app --reload
```

5. Open your browser and go to `http://localhost:8000` and you should see the following response:

```json
{ "Hello": "World" }
```

6. To stop the server, press `Ctrl+C` in the terminal.
