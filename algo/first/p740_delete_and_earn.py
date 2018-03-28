from collections import Counter


class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slots = Counter(nums)
        rob_previous = 0
        rob_current = 0
        for val in range(10001):
            rob_previous, rob_current = rob_current, max(rob_previous + val * slots[val], rob_current)

        return max(rob_previous, rob_current)
