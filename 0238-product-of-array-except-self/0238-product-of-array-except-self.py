class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = nums[0]
        lp = [1, product]
        for i in range(1, len(nums)- 1):
            lp.append(nums[i] * product)
            product *= nums[i]
        product = nums[len(nums) - 1]
        rp = [1, product]
        for i in range(len(nums) - 2, 0, -1):
            rp.append(nums[i] * product)
            product *= nums[i]
        
        for i in range(0, len(nums)):
            nums[i] = lp[i] * rp[len(nums)-i-1]
        return nums