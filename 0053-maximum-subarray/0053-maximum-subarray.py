class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         [-2, -1, -4, 0, -1, 1, 2, -3, 1]
#         [5, 9, 8, 15, 23]
        if len(nums) == 1:
            return nums[0]
        maximum = 0
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
            if nums[i] > nums[maximum]:
                maximum = i
        
        return nums[maximum]
            
        