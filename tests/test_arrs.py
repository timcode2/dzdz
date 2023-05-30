import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -5, "test") == "test"
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]

def test_slice_with_start_greater_than_length():
    assert arrs.my_slice([1, 2, 3], 5) == []
    assert arrs.my_slice([1, 2, 3], 10) == []

def test_slice_with_negative_start():
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]