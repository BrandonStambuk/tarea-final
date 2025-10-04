import requests

def test_get_users(config_test):
    url = f"{config_test['base_url']}/admin/users"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {config_test['api_key']}"
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Status code incorrecto: {response.status_code}"
    data = response.json()
    assert len(data) > 0, "No hay usuarios en la respuesta"
    
