class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n, s = len(matchsticks), sum(matchsticks)
        if s % 4: return False
        target = s // 4
        matchsticks.sort(reverse = True)
        used = [False] * len(matchsticks)
        def dfs(start, sides, curr):
            if sides == 4:
                return True
            if curr == target:
                return dfs(0, sides + 1, 0)
            for i in range(start, n):
                if ((i and not used[i - 1] and matchsticks[i] == matchsticks[i - 1]) or 
                    (used[i] or curr + matchsticks[i] > target)):
                    continue
                used[i] = True
                if dfs(i + 1, sides, curr + matchsticks[i]):
                    return True
                used[i] = False
                if curr == 0:
                    break
        return dfs(0, 0, 0)