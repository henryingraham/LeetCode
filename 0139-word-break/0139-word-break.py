class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = {}
        def helper(s, wordDict, memo):
            if s in memo:
                return memo[s]
            if s == '':
                return True
            
            for word in wordDict:
                if s.find(word) == 0:
                    suffix = s[len(word):]
                    if helper(suffix, wordDict, memo):
                        memo[s] = True
                        return True
            memo[s]=False
            return False
        
        return helper(s, wordDict, memo)
