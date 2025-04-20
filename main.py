# main.py

def palindrome(string):
    """Returns True if input is a palindrome, otherwise False."""
    if not string and string != 0:
        err = "Invalid input"
        raise ValueError(err)

    string = str(string).lower()

    return string == string[::-1]
