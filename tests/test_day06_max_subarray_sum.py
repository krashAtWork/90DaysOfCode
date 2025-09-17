import pytest
from problems.day06_max_subarray_sum import get_max_subarray_sum

def test_all_positive():
    assert get_max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_all_negative():
    assert get_max_subarray_sum([-1, -2, -3, -4]) == -1

def test_mixed_numbers():
    assert get_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    

def test_single_element():
    assert get_max_subarray_sum([7]) == 7

def test_empty_list():
    assert get_max_subarray_sum([]) == 0

def test_large_negative_then_positive():
    assert get_max_subarray_sum([-10, 2, 3, -2, 5, -1]) ==8

def test_all_zeros():
    assert get_max_subarray_sum([0, 0, 0, 0]) == 0

def test_subarray_at_end():
    assert get_max_subarray_sum([-3, -2, 5, 6]) == 11

def test_subarray_at_start():
    assert get_max_subarray_sum([5, 6, -10, 2]) == 11