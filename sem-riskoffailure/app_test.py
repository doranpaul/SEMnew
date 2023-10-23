import pytest
from app import app

#@pytest.fixture to build up mock client to be used in tests
@pytest.fixture
def client():
    return app.test_client()

def test_valid_input_no_risk_of_fail(client):
    response = client.get('/?item_1=undefined&attendance_1=30&item_2=undefined&attendance_2=20&item_3=undefined&attendance_3=40&item_4=undefined&attendance_4=50&cut-off=50')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["riskOfFail"] == "Student is not currently at risk of failure"

def test_valid_input_risk(client):
    response = client.get('/?item_1=undefined&attendance_1=10&item_2=undefined&attendance_2=10&item_3=undefined&attendance_3=10&item_4=undefined&attendance_4=15&cut-off=75')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["riskOfFail"] == "Student is currently failing, you need to improve your attendance!"
    
def test_invalid_arg_type(client):
    response = client.get('/?item_1=undefined&attendance_1=yes&item_2=undefined&attendance_2=20&item_3=undefined&attendance_3=40&item_4=undefined&attendance_4=50&cut-off=50')
    assert response.status_code == 400
    assert b"Invalid request. Attendance values and cut-off must be integers." in response.data 

def test_missing_arg(client):
    response = client.get('/?item_1=undefined&attendance_1=&item_2=undefined&attendance_2=20&item_3=undefined&attendance_3=40&item_4=undefined&attendance_4=50&cut-off=50')
    assert response.status_code == 400
    assert b"Invalid request. Attendance values and cut-off must be integers." in response.data

def test_out_of_range(client):
    response = client.get('/?item_1=undefined&attendance_1=50&item_2=undefined&attendance_2=50&item_3=undefined&attendance_3=60&item_4=undefined&attendance_4=70&cut-off=50')
    assert response.status_code == 400
    assert b"Invalid request. Attendance values or cut-off is out of range." in response.data