class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        if rows < 3 or cols < 3:
            return 0
        
        count = 0
        
        def isMagicSquare(r,c) -> bool:
            nums = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if 0 < grid[i][j] < 10:
                        nums.add(grid[i][j])
            if len(nums) != 9:
                return False
                    
            topRow = sum([grid[r][c], grid[r][c+1], grid[r][c+2]])
            middleRow = sum([grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2]])
            bottomRow = sum([grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]])
            leftCol = sum([grid[r][c], grid[r+1][c], grid[r+2][c]])
            middleCol = sum([grid[r][c+1], grid[r+1][c+1], grid[r+2][c+1]])
            rightCol = sum([grid[r][c+2], grid[r+1][c+2], grid[r+2][c+2]])
            diag1 = sum([grid[r][c], grid[r+1][c+1], grid[r+2][c+2]])
            diag2 = sum([grid[r+2][c], grid[r+1][c+1], grid[r][c+2]])
            
            if topRow == middleRow == bottomRow == leftCol == middleCol == rightCol == diag1 == diag2:
                return True
            return False
        
        for r in range(0, rows + 1 - 3):
            for c in range(0, cols + 1 - 3):
                if isMagicSquare(r,c):
                    count += 1
            
        return count
        