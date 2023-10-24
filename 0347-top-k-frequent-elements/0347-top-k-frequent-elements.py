class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(lambda: 0)
        
        for num in nums:
            d[num] += 1
        s = sorted(d.items(), key=lambda x:x[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(s[i][0])
        return res
            