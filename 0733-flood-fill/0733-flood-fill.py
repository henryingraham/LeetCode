class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not image:
            return image;
        match = image[sr][sc]
        visited = set()
        rows, cols = len(image), len(image[0])
        def fill(r,c):
            if r < 0 or r == rows or c < 0 or c == cols or image[r][c] != match or (r,c) in visited:
                return 0
            image[r][c] = color
            visited.add((r,c))
            fill(r+1,c)
            fill(r-1,c)
            fill(r,c-1)
            fill(r,c+1)
        fill(sr,sc)
        print(visited)
        return image