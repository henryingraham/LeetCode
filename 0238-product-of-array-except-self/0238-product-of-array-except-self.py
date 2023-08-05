class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = nums[0]
        lp = [0, product]
        for i in range(1, len(nums)- 1):
            lp.append(nums[i] * product)
            product *= nums[i]
        product = nums[len(nums) - 1]
        rp = [product, 0]
        for i in range(len(nums) - 2, 0, -1):
            rp.insert(0, nums[i] * product)
            product *= nums[i]
        
        for i in range(1, len(nums) - 1):
            nums[i] = lp[i] * rp[i]
        nums[0] = rp[0]
        nums[len(nums) - 1] = lp[len(lp) - 1]
        return nums