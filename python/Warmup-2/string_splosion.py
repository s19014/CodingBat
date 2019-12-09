'''Given a non-empty string like "Code" return a string like "CCoCodCode".'''


def string_splosion(str):
    c = ''
    for i in range(len(str)):
        c += str[:i+1]
    return c
