from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/api/items/", json={"name": "Item 1", "price": 10.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Item 1"
    assert response.json()["price"] == 10.0

def test_list_items():
    response = client.get("/api/items/")
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_get_item_by_id():
    response = client.get("/api/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Item 1"

def test_update_item():
    response = client.put("/api/items/1", json={"name": "Updated Item", "price": 15.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"
    assert response.json()["price"] == 15.0

def test_delete_item():
    response = client.delete("/api/items/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted successfully"

def test_transform_prices():

    client.post("/api/items/", json={"name": "Item 1", "price": 10.0})
    client.post("/api/items/", json={"name": "Item 2", "price": 20.0})


    response = client.post("/api/items/transform-prices/", json={"transform_type": "tax", "items": [1, 2]})
    assert response.status_code == 200
    assert response.json()[0]["price"] == 11.0
    assert response.json()[1]["price"] == 22.0