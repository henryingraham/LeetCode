class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            if target-nums[i] in s.keys():
                return [i, s[target-nums[i]]]
            else:
                s[nums[i]] = i