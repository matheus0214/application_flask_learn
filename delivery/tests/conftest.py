import pytest

from delivery.app import create_app


@pytest.fixture(scope="module")
def app():
    """Instance app flask"""
    return create_app()
