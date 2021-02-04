import re


def is_poly(s):
    """
    Returns True if s is a Palindrome
    """

    def clean(s):
        regex = re.compile('[^a-zA-Z0-9]')  # removes all but letters and digits
        return regex.sub('', s)

    return clean(s).lower() == clean(s).lower()[::-1]


print(is_poly("A man, a plan, a canal: Panama"))
print(is_poly("madam"))
print(is_poly("0P"))
