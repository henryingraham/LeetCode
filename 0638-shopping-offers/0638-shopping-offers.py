class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        memo = {}
        
        def dp(needs):
            if needs in memo:
                return memo[needs]
            
            cost = sum(price[i] * needs[i] for i in range(len(needs)))
            
            for offer in special:
                remain = [needs[i] - offer[i] for i in range(len(needs))]
                
                if all(x >= 0 for x in remain):
                    cost = min(cost, offer[-1] + dp(tuple(remain)))
            
            memo[needs] = cost
            return cost
        
        return dp(tuple(needs))