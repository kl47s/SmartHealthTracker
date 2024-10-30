import pytest
from src.shared.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_data(client):
    response = client.post('/health', json={'steps': [1000, 2000, 3000], 'sleep': [6, 7, 8]})
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'average_steps' in json_data
    assert json_data['average_steps'] == 2000.0
