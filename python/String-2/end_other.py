'''Given two strings, return True if either of the strings appears at the very
end of the other string, ignoring upper/lower case differences (in other words,
the computation should not be "case sensitive"). Note: s.lower() returns the
lowercase version of a string.'''


def end_other(a, b):
    def end_character(long_s, short_s):
        return short_s.lower() == long_s.lower()[-(len(short_s)):]
    return end_character(a, b) or end_character(b, a)
