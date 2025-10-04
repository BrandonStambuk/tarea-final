import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def config_test():
    return {
        "base_url": os.getenv("BASE_URL_API"),
        "api_key": os.getenv("API_KEY"),
    }
