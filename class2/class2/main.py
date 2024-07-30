from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/piaic")
def piaic():
    return {"organization": "PIAIC"}