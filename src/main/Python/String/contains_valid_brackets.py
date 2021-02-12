# Question:
"""
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', (example: s = '{{{()}[]}}')
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

Input: s = '{{{()}[]}}'
Output: true

"""


# Solution 1
def is_valid(s: str) -> bool:
    if s == '':
        return False

    s_copy = []
    for item in s:
        s_copy.append(item)

    print(s_copy)
    print(len(s_copy))
    flag = False

    i = 0
    while i < (len(s_copy) - 1):
        if s_copy[i] == '(' and s_copy[i + 1] == ')' or \
                s_copy[i] == '[' and s_copy[i + 1] == ']' or \
                s_copy[i] == '{' and s_copy[i + 1] == '}':
            flag = True
            s_copy.pop(i)
            s_copy.pop(i)
            i = -1

            if len(s_copy) == 0:
                return True
        i += 1

    if len(s_copy) >= 1:
        return False
    else:
        return flag


def is_valid2(s: str) -> bool:
    if len(s) <= 1:
        return False

    stack = []
    for ch in s:
        # If open brackets, push onto the stack
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        # if close ')' pop and compare the pair to be opposite version of it
        elif ch == ')' and stack and stack.pop() == '(':
            continue
        # if close '}' pop and compare the pair to be opposite version of it
        elif ch == '}' and stack and stack.pop() == '{':
            continue
        # if close ']' pop and compare the pair to be opposite version of it
        elif ch == ']' and stack and stack.pop() == '[':
            continue
        # If the above condition is not true, then its not valid
        else:
            return False

    return True if not stack else False


s = '{{{()}[]}}'
print(is_valid2(s))
