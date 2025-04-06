# TODO: FastAPI backend code
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Hello from SmartRoom backend"}
