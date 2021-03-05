import string


# Question at: leetcode ( t.ly/mevY )
def minRemoveToMakeValid(s: str) -> str:
    if len(s) <= 1:
        return s

    l = []
    for i in range(len(s)):
        l.append(s[i])

    i = 0
    open_counter = 0
    A = string.ascii_lowercase
    result = []

    while i < len(l):
        # If open brackets, push onto the result
        t = l[i]
        if l[i] in {'(', '{', '['}:
            open_counter += 1
            result.append(l[i])

        elif l[i] == ')' and result and open_counter > 0:
            open_counter -= 1
            result.append(l[i])
            continue

        elif l[i] == '}' and result and open_counter > 0:
            open_counter -= 1
            result.append(l[i])
            continue

        elif l[i] == ']' and result and open_counter > 0:
            open_counter -= 1
            result.append(l[i])
            continue

        elif l[i] in A:
            result.append(l[i])

        elif l[i] in {')', ']', '}'} and open_counter > 1:
            l.remove(l[i])
            open_counter -= 1
            i -= 1

        i += 1

    for item in reversed(range(len(result))):
        print(item, result[item])
        if result[item] in {'(', '[', '{'} and open_counter > 0:
            result = result[:item] + result[item + 1:]
            open_counter -= 1

    # for item in reversed(l):
    #     if item in {'(', '[', '{'} and open_counter > 0:
    #         l.remove(item)
    #         open_counter -= 1

    return ''.join(str(e) for e in result)


"""
Convert string to list, because String is an immutable data structure in Python and it's much easier and memory-efficient to deal with a list for this task.
Iterate through list
Keep track of indices with open parentheses in the stack. In other words, when we come across open parenthesis we add an index to the stack.
When we come across close parenthesis we pop an element from the stack. If the stack is empty we replace current list element with an empty string
After iteration, we replace all indices we have in the stack with empty strings, because we don't have close parentheses for them.
Convert list to string and return
Time complexity is O(n)
Memory complexity is O(n)
(https://is.gd/X10l8p)
"""


def minRemoveToMakeValid2(s: str) -> str:
    s = list(s)
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    while stack:
        s[stack.pop()] = ''
    return ''.join(s)


s = "(a(b(c)d)"

print(minRemoveToMakeValid2(s))
