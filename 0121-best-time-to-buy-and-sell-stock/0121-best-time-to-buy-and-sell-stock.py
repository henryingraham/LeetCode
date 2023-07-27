class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            if prices[right] - prices[left] > maxProfit:
                maxProfit = prices[right] - prices[left]
            if prices[left] >= prices[right]:
                left = right
            right += 1
            
        return maxProfit