import pytest, requests

def test_api_get_functionality():
    base_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(base_url, timeout=30)
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
    assert isinstance(data,list)
    assert isinstance(data[0],dict)
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]
    assert "userId" in data[0]

def test_api_post_functionality():
    base_url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "userId": 5,
        "title": "This is not the post you're looking for",
        "body": "You want to go home & re-think your life"
    }

    response = requests.post(base_url,json=payload,timeout=30)
    assert response.status_code == 201

    json_response = response.json()
    assert json_response["userId"] == 5
    assert json_response["title"] == payload["title"]
    assert json_response["body"] == payload["body"]
    assert "id" in json_response

def test_api_get_negative():
    base_url = "https://jsonplaceholder.typicode.com/posts/999999999"
    response = requests.get(base_url, timeout=30)

    assert response.status_code == 404