import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]

def test_get_cities_for_non_existent_country():
    response = client.get('/countries/Denmark/cities')
    assert response.status_code == 200
    assert response.json() == {'error': 'Country not found'}

def test_get_cities_for_spain():
    response = client.get('/countries/Spain/cities')
    assert response.status_code == 200
    assert "Seville" in response.json()


def test_monthly_average_for_seville_in_january():
    response = client.get('/countries/Spain/Seville/January')
    assert response.status_code == 200
    assert response.json() == {'high': 61, 'low': 41}  # Example data, adjust as needed
