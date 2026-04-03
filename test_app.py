import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_view_count(client):
    # First visit to /
    response1 = client.get('/')
    assert response1.status_code == 200
    assert 'viewed <strong>1</strong> times' in response1.data.decode()
    
    # Second visit to /
    response2 = client.get('/')
    assert response2.status_code == 200
    assert 'viewed <strong>2</strong> times' in response2.data.decode()
    
    # Visit to /home
    response3 = client.get('/home')
    assert response3.status_code == 200
    assert 'viewed <strong>2</strong> times total' in response3.data.decode()