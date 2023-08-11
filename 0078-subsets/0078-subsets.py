class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        memo = [[]]
        
        
        for i in range(len(nums)):
            for j in range(len(memo)):
                temp = memo[j].copy()
                temp.append(nums[i])
                memo.append(temp)

        return memo