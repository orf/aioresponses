import pytest
from aioresponses import aioresponses


@pytest.fixture
def aioresponse():
    with aioresponses() as m:
        yield m
