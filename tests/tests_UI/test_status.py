import json
import pytest
from faker import Faker
from pages.employement_status_page import StatusPage

with open("data/status_data.json") as f:
    status_data = json.load(f)

faker = Faker()

@pytest.mark.parametrize("status_name", [faker.job() for _ in range(2)]) 
def test_add_status_faker(page_logged, status_name):
    sp = StatusPage(page_logged.page)  
    sp.goto()  
    assert sp.add_status(status_name)



@pytest.mark.parametrize("status",status_data) 
def test_add_status_json(page_logged, status):
    sp = StatusPage(page_logged.page)  
    sp.goto()  
    assert sp.add_status(status["name"])