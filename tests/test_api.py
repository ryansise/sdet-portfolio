import pytest, requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("REQRES_API_KEY")
BASE_URL = os.getenv("REQRES_BASE_URL")

@pytest.mark.skipif(not API_KEY, reason="REQRES_API_KEY not set")
def test_authenticated_endpoint():
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(f"{BASE_URL}", headers=headers, timeout=30)
    assert response.status_code == 200
    response_invalid = requests.get(f"{BASE_URL}", timeout=30)
    assert response_invalid.status_code == 401

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

#def test_api_get_negative():

    