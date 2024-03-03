import sys, os

sys.path.insert(0, os.path.abspath("."))
from fastapi.testclient import TestClient
from main.apps.microservice.main import app

client = TestClient(app)


def test_get_characters():
    response = client.get("/characters")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Character 1"},
        {"id": 2, "name": "Character 2"},
        {"id": 3, "name": "Character 3"},
    ]


def test_create_character():
    response = client.post("/characters")
    assert response.status_code == 200
    assert response.json() == {"id": 4, "name": "New Character"}


def test_update_character():
    character_id = 1
    response = client.put(f"/characters/{character_id}")
    assert response.status_code == 200
    assert response.json() == {"id": character_id, "name": "Updated Character"}


def test_delete_character():
    character_id = 1
    response = client.delete(f"/characters/{character_id}")
    assert response.status_code == 200
    assert response.json() == {"id": character_id, "name": "Deleted Character"}
