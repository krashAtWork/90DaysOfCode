import pytest
from problems.day01_reverse_string import reverse_string01, reverse_string02

pair = ("love", reverse_string02("love"))

@pytest.mark.parametrize("input, output", 
                         [("apple", 'elppa'),
                          pair,
                          ("i", "i")])
def test_reverse_string(input, output):
    assert  reverse_string01(input) == output

