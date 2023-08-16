class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxprof = 0
        for i in range(1, len(prices)):
            maxprof = max(maxprof, prices[i] - mini)
            mini = min(mini, prices[i])
        return maxprof
                