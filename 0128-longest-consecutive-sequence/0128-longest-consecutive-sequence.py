class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        m = 0
        visited = set()
        s = set(nums)
        
        for num in nums:
            if not num in visited:
                count = 0
                r = num
                l = num-1
                while r in s:
                    count+=1
                    visited.add(r)
                    r+=1
                while l in s:
                    count+=1
                    visited.add(l)
                    l-=1
                m = max(count, m)
            
        return m
        