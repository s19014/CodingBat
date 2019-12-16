'''We want make a package of goal kilos of chocolate. We have small bars
(1 kilo each) and big bars (5 kilos each). Return the number of small bars to
use, assuming we always use big bars before small bars. Return -1 if it can't
be done.'''


def make_chocolate(small, big, goal):
    n = goal // 5
    diff = goal - 5 * min(n, big)
    answer = small if diff == small else (diff if diff < small else -1)
    return answer
