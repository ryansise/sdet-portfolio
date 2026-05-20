import pytest, requests

def test_api():
    baseURL = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(baseURL)
    assert response.status_code == 200