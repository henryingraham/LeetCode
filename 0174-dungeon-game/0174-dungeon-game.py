class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        r = len(dungeon)
        c = len(dungeon[0])
        
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if i == r-1 and j == c-1:
                    dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
                elif i == r-1:
                    dungeon[i][j] = max(dungeon[i][j+1] - dungeon[i][j], 1)
                elif j == c-1:
                    dungeon[i][j] = max(dungeon[i+1][j] - dungeon[i][j], 1)
                else:
                    dungeon[i][j] = max(min(dungeon[i][j+1], dungeon[i+1][j]) - dungeon[i][j], 1)
        return dungeon[0][0]