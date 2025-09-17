# Write a function to reverse a string.


# string is a list of characters.

# apple -> elppa - 5 -0-4
def reverse_string01(str):
    result =""
    for i in range(len(str) -1, -1, -1):
        result += str[i]
        print(str[i])
    return result

def reverse_string02(str):
    original_str = str
    reverse_str = "".join(reversed(str))
    return reverse_str

print(reverse_string02('apple'))








# LEARN
# to install packages from requirements.txt - pip install -r requirements.txt
# HINT: You are attempting to install a package literally named "requirements.txt" (which cannot exist).
#  Consider using the '-r' flag to install the packages listed in requirements.txt