import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("test_search.log"), logging.StreamHandler()])

BASE_URL = "http://127.0.0.1:8080"
AUTH_ENDPOINT = f"{BASE_URL}/auth"
CARS_ENDPOINT = f"{BASE_URL}/cars"

USERNAME = "test_user"
PASSWORD = "test_pass"


@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    assert response.status_code == 200, "Аутентифікація не вдалася"
    access_token = response.json().get("access_token")
    assert access_token, "Не отримано токен доступу"

    session.headers.update({'Authorization': f'Bearer {access_token}'})
    logging.info("Успішна аутентифікація")
    return session


@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 10),
    ("engine_volume", 7),
    ("brand", 10),
    ("price", 15),
])

def test_get_cars(auth_session, sort_by, limit):
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit:
        params["limit"] = limit

    response = auth_session.get(f"{BASE_URL}/cars", params=params)
    assert response.status_code == 200, "Не вдалося отримати список автомобілів"
    data = response.json()

    assert isinstance(data, list), "Відповідь повинна бути списком"
    if limit:
        assert len(data) <= limit, f"Очікувалось не більше {limit} записів"

    if sort_by:
        values = [car[sort_by] for car in data]
        assert values == sorted(values), f"Список не відсортований за {sort_by}"

    logging.info(f"Тест пройдено: sort_by={sort_by}, limit={limit}, records={len(data)}")
