import pytest
from problems.day04_substring_search import isSubStringPresent

def test_substring_present():
    assert isSubStringPresent("hello world", "world") is True  # function does not return True/False

def test_substring_not_present():
    assert isSubStringPresent("hello world", "python") is False

def test_substring_at_start():
    assert isSubStringPresent("abcdef", "abc") is True

def test_substring_at_end():
    assert isSubStringPresent("abcdef", "def") is True

def test_substring_full_string():
    assert isSubStringPresent("abcdef", "abcdef") is True

def test_empty_substring():
    assert isSubStringPresent("abcdef", "") is True

def test_empty_main_string():
    assert isSubStringPresent("", "abc") is False

def test_both_empty():
    assert isSubStringPresent("", "") is True