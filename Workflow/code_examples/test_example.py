import pytest
import numpy as np


# example_test.py
def test_add_numbers():
    result = np.add(2, 3)
    assert result == 5


def test_empty_list():
    my_list = []
    assert len(my_list) == 0
    assert not my_list


@pytest.fixture
def sample_data():
    return {"name": "Test", "value": 42}
