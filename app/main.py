from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/health")
def health():
    return {"status": "ok"}