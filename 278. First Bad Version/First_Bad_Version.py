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
        lower = 1
        upper = n
        bad = n
        while(lower <= upper):
            mid = floor((lower+upper)/2)
            if isBadVersion(mid):
                bad = min(bad,mid)
                upper = mid-1
            else:
                lower = mid+1
        return int(bad)
            