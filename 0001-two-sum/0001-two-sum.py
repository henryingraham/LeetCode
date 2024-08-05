class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        mem = {}
        for i in range(0,len(nums)):
            if (target-nums[i] in mem.keys()):
                ans.append(mem[target-nums[i]])
                ans.append(i)
                return ans
            else:
                mem[nums[i]] = i
