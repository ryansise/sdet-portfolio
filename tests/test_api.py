import pytest, requests
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def auth_session():
    api_key = os.getenv("REQRES_API_KEY")
    base_url = os.getenv("REQRES_BASE_URL")
    assert api_key, "REQRES_API_KEY is required"
    assert base_url, "REQRES_BASE_URL is required"
    session = requests.Session()
    session.headers.update({
        "x-api-key": api_key,
        "Content-Type": "application/json"
    })
    return session,base_url


def test_authenticated_endpoint(auth_session):
    session,base_url = auth_session
    response = session.get(base_url, timeout=30)
    assert response.status_code == 200
    
def test_auth_endpoint_no_key():
    url = os.getenv("REQRES_BASE_URL")
    response = requests.get(url, timeout=30)
    assert response.status_code in (401, 403)

def test_api_get_functionality(auth_session):
    session,base_url = auth_session
    response = session.get(base_url, timeout=30)
    data = response.json()
    assert len(data) > 0
    assert isinstance(data,dict)
    assert "collection_id" in data["data"][0]
    assert "name" in data["data"][0]["data"]
    assert "category" in data["data"][0]["data"]
    assert "price" in data["data"][0]["data"]
    assert "in_stock" in data["data"][0]["data"]

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

    