'''We want to make a row of bricks that is goal inches long. We have a number
of small bricks (1 inch each) and big bricks (5 inches each). Return True if
it is possible to make the goal by choosing from the given bricks. This is a
little harder than it looks and can be done without any loops. See
also: Introduction to MakeBricks'''


def make_bricks(small, big, goal):
    num = goal // 5
    if num <= big:
        return goal - num * 5 <= small
    else:
        return goal - big * 5 <= small
    return False
