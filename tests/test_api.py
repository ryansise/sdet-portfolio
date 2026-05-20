import pytest, requests

def test_api():
    baseURL = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(baseURL)
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
    assert isinstance(data,list)
    assert isinstance(data[0],dict)
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]
    assert "userId" in data[0]