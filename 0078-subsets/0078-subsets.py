class Solution(object):
    def subsets(self, nums):
        memo = [[]]
        
        for num in nums:
            for i in range(len(memo)):
                memo.append(memo[i]+[num])
        return memo
        
        