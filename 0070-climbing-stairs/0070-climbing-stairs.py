class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = {}
        res[1], res[2], res[3] = 1, 2, 3
        for i in range(4, n + 1):
            res[i] = res[i-1] + res[i-2]
        return res[n]