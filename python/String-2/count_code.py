'''Return the number of times that the string "code" appears anywhere in the
given string, except we'll accept any letter for the 'd', so "cope" and "cooe"
count.'''


def count_code(str):
    cnt = 0
    for i in range(len(str) - 3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            cnt += 1
    return cnt
