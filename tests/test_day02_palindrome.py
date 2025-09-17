import pytest
from problems.day02_palindrome import isPalindrome

@pytest.mark.parametrize("inpu, outpu",[ 
    ("palindrome", False),
    ("malayalam", True),
    ("1001", True),
    ("a", True),
    ("krashagi", False)])
def test_palindrome(inpu, outpu):
    assert isPalindrome(inpu) == outpu


# LEARN
# if we don't put annotation @ 
#This error is thrown
# ______________________ ERROR at setup of test_palindrome _______________________
# file /Users/krashagigupta/Learning/sharp-practice/tests/test_day02_palindrome.py, line 9
#   def test_palindrome(inpu, outpu):
# E       fixture 'inpu' not found
# >       available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, doctest_namespace, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
# >       use 'pytest --fixtures [testpath]' for help on them.