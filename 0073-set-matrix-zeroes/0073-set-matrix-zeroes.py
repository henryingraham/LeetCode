class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        
        def zero(r, c):
            for i in range(rows):
                if matrix[i][c] != 0:
                    matrix[i][c] = '#'
            for j in range (cols):
                if matrix[r][j] != 0:
                    matrix[r][j] = '#'
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero(r,c)
                    
        for r in range(rows):
            for c in range(cols):
                    if matrix[r][c] == '#':
                        matrix[r][c] = 0
        return matrix