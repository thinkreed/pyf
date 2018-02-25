# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low < high:
            mid = low + ((high - low) >> 1)
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low
