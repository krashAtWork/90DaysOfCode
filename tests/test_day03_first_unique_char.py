import pytest
from problems.day03_first_unique_char import firstUniqueChar

def test_single_character():
    assert firstUniqueChar("a") == "a"

def test_all_unique():
    assert firstUniqueChar("abc") == "a"

def test_first_unique_in_middle():
    assert firstUniqueChar("aabbc") == "c"

def test_no_unique_character():
    assert firstUniqueChar("aabbcc") is False

def test_first_unique_at_end():
    assert firstUniqueChar("aabbc") == "c"

def test_empty_string():
    with pytest.raises(IndexError):
        firstUniqueChar("")

def test_mixed_case():
    assert firstUniqueChar("aAbBcC") == "a"

def test_numbers_and_letters():
    assert firstUniqueChar("112233a") == "a"

def test_special_characters():
    assert firstUniqueChar("!!@@#") == "#"