# --------------------------------------------------------------------------------------------------
# Include(s)
# --------------------------------------------------------------------------------------------------
from ..src.app import app
import pytest


# --------------------------------------------------------------------------------------------------
@pytest.fixture
def client():
    """
    A test client for the app.
    """

    with app.test_client() as client:
        yield client


# --------------------------------------------------------------------------------------------------
def test_home_page(client):
    """
    Test that the home page returns what's expected.
    """

    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Hello World!"}
