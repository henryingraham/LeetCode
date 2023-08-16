class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        maxprof = 0
        buy = prices[0]
        for s in prices[1:]:
            if s > buy: 
                if s - buy > maxprof:
                    maxprof = s - buy
            else:
                buy = s
        return maxprof
                