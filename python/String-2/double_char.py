'''Given a string, return a string where for every char in the original, there
are two chars.'''


def double_char(str):
    li = []
    for i in range(len(str)):
        li.append(str[i] * 2)
    return ''.join(li)
