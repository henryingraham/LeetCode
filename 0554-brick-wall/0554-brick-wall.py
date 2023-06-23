class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        frequency = {}
        max_slices = 0
        for row in wall:
            cur_pos = 0
            for brick in range(0, len(row) - 1):
                cur_pos += row[brick]
                if cur_pos in frequency:
                    frequency[cur_pos] = frequency[cur_pos] + 1
                else:
                    frequency[cur_pos] = 1
                if frequency[cur_pos] > max_slices:
                    max_slices = frequency[cur_pos]
        return len(wall) - max_slices