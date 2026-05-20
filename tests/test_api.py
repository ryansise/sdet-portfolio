import pytest, requests

def test_api():
    baseURL = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(baseURL, timeout=30)
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
    assert isinstance(data,list)
    assert isinstance(data[0],dict)
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]
    assert "userId" in data[0]
    assert "name" not in data[0]

def add_post():
    baseURL = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "userId": 5,
        "id": 15,
        "title": "This is not the post you're looking for",
        "body": "You want to go home & re-think your life"
    }
    response = requests.post(baseURL,json=payload)
    assert response.status_code == 201

    json_response = response.json()
    assert json_response["userId"] == 5
    assert json_response["id"] == 15