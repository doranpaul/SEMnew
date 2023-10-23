import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_valid_input(client):
    response = client.get('/?attendance_1=10&attendance_2=15&attendance_3=20&attendance_4=25')
    assert response.status_code == 200
    json_data = response.get_json()
    assert isinstance(json_data["improvement_plan"], list)

def test_invalid_arg_type(client):
    response = client.get('/?attendance_1=hello&attendance_2=15&attendance_3=20&attendance_4=25')
    assert response.status_code == 400
    assert b"Invalid request. Attendance values and cut-off must be integers." in response.data

def test_missing_arg(client):
    response = client.get('/?attendance_1=10&attendance_2=15&attendance_3=20')
    assert response.status_code == 400
    assert b"Invalid request. Attendance values and cut-off must be integers." in response.data

def test_out_of_range(client):
    response = client.get('/?attendance_1=40&attendance_2=15&attendance_3=20&attendance_4=25')
    assert response.status_code == 400
    assert b"Invalid request. Attendance values are out of range." in response.data
