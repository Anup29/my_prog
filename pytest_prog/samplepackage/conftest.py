import pytest


@pytest.fixture(autouse=True,scope="session")
def setup_and_teardown():
    print("Lanuch Browser")
    print("Open App")
    yield
    print("Close App")
    print("Close Browser")
