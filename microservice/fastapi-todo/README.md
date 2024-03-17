```bash
poetry new fastapi-todo --name src
```

```bash
poetry add fastapi "uvicorn[standard]" sqlmodel psycopg pytest httpx
```

```bash
poetry run uvicorn src.main:app --reload
```
