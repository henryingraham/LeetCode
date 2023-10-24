class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1 for _ in range(len(nums))]
        rp = [1 for _ in range(len(nums))]
        
        for i in range(1, len(lp)):
            lp[i] = lp[i-1]*nums[i-1]
            rp[-i-1] = rp[-i]*nums[-i]
        
        res = []
        for i in range(0, len(lp)):
            res.append(lp[i]*rp[i])
            
        return res
        