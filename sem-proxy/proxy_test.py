import json
import pytest
import requests_mock
from proxy import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_invalid_service(client):
    res = client.get('/invalid-service')
    assert res.status_code == 400
    assert res.data.decode('utf-8') == "Invalid service name"

def test_valid_service(client):
    with requests_mock.Mocker() as m:
        service_name = 'sem-maxmin'
        mock_url = "http://sem-maxmin.40070680.qpc.hal.davecutting.uk"
        m.get(mock_url, text='mocked_response', status_code=200)

        res = client.get(f'/{service_name}')

        assert res.status_code == 200
        assert res.data.decode('utf-8') == "mocked_response"
