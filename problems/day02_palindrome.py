# check if a string is a palindrome
from utils.handy import reverse_string02


'''A palindrome is a string that looks the same in the reverse order'''
# we can use the reverse function we just made or python inbuilt reversed
def isPalindrome(st):
    if reverse_string02(st) == st:
        return True
    else: 
        return False