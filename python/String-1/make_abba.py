'''Given two strings, a and b, return the result of putting them together in
the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".'''


def make_abba(a, b):
    return "{0}{1}{1}{0}".format(a, b)
