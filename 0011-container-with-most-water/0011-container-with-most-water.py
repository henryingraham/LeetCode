class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            width = right - left
            minHeight = min(height[left], height[right])
            current = minHeight * width 
            maxArea = max(current, maxArea)

            if height[right] > height[left]:
              left += 1
            else:
              right -= 1
        return maxArea