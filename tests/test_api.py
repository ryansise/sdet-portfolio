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
    session.headers.update(
        {
            "x-api-key": api_key,
            "Content-type": "application/json"
        }
    )
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
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,dict)
    assert "data" in data
    assert isinstance(data["data"],list)
    assert len(data["data"]) > 0

    item = data["data"][0]
    assert isinstance(item,dict)

    if "collection_id" in item:
        assert "app_user_id" in item
        assert "project_id" in item

    nested = item.get("data",item)
    assert "name" in nested
    assert "category" in nested
    assert "price" in nested
    assert "in_stock" in nested

def test_api_post_functionality(auth_session):
    session,base_url = auth_session
    payload = {
        "data": {
            "name": "Widget",
            "category": "Electronics",
            "price": 25.99,
            "in_stock": True
        }
    }

    response = session.post(base_url, json=payload, timeout=30)
    assert response.status_code in (200,201)

    json_response = response.json()
    assert isinstance(json_response,dict)
    assert "data" in json_response

    created = json_response["data"]["data"]
    assert created["name"] == payload["data"]["name"]
    assert created["category"] == payload["data"]["category"]
    assert created["price"] == payload["data"]["price"]
    assert created["in_stock"] == payload["data"]["in_stock"]

def test_api_get_negative(auth_session):
    session,base_url = auth_session

    bad_url = f"{base_url[:-len('?project_id=24036')]}/not-gonna-work"
    response = session.get(bad_url, timeout=30)
    assert response.status_code == 404

    