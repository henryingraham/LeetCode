class Solution:
    def countBits(self, n: int) -> List[int]:
        d = {}
        res = []
        d[0] = 0
        res.append(d[0])
        if n == 0:
            return res
        for i in range(1, n+1):
            if i % 2 == 0:
                d[i] = d[i/2]
                res.append(d[i])
            else:
                d[i] = d[i - 1] + 1
                res.append(d[i])
        
        return res