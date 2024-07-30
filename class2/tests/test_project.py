from fastapi.testclient import TestClient
from class2.main import app

def test_root():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
def test2():
    client = TestClient(app=app)
    response = client.get("/piaic")
    assert response.status_code == 200
    assert response.json() == {"organization": "PIAIC"}