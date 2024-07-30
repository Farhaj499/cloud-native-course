# FastAPI app

Adding the fastapi app to your project
-> poetry add fastapi

Server to run fastapi app
-> poetry add "uvicorn[standard]"

importing in main.py
from fastapi import FastAPI

creating an object of FastAPI
app = FastAPI() 

creating main route
@app.get("/")
def hello():
    return {"Hello": "World"}

@ decorator function
If ("/") is accessed/true, it will automatically call the function below it

To run the app on the sever:localhost/8000
-> poetry run uvicorn class2.main:app --reload

To test fastAPI app, we create a file will prefix "test" in it and import TestClient from fastapi.testclient. We use pytest for testing.

