import pytest
from config.config import BASE_URL

@pytest.fixture(scope='session')
def api_base_url():
   return BASE_URL;