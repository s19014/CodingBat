'''Given 2 ints, a and b, return True if one if them is 10 or if their sum is
10.'''


def makes10(a, b):
    return 10 in [a, b] or a + b == 10
