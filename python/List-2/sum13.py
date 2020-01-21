'''Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that
come immediately after a 13 also do not count.'''


def sum13(nums):
    for i in range(len(nums)-1):
        if nums[i] == 13:
            nums[i+1] = 0
    return sum(nums) - 13 * nums.count(13)
