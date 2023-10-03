class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        visited = set()
        
        def fill(r,c,val):
            if r >=rows or r < 0 or c >= cols or c < 0 or (r,c) in visited or image[r][c] != val:
                return 0
            image[r][c] = color
            visited.add((r,c))
            
            fill(r+1,c,val)
            fill(r-1,c,val)
            fill(r,c+1,val)
            fill(r,c-1,val)
            
        fill(sr,sc, image[sr][sc])
        
        
        return image