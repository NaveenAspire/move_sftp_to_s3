import pytest

@pytest.fixture
def obj_body():
    return b'binary data'

@pytest.fixture
def key_name():
    return '<key_name>'