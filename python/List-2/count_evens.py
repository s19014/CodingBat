'''Return the number of even ints in the given array. Note: the % "mod"
operator computes the remainder, e.g. 5 % 2 is 1.'''


def count_evens(nums):
    return len([n for n in nums if n % 2 == 0])
