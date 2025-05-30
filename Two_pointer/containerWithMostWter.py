class Solution(object):
    def maxArea(self, height):
        n = len(height)
        area = 0
        maxArea = float("-inf")
        low = 0
        high = n - 1
        while low < high:
            if height[low] > height[high]:
                maxHeight = height[low]
                minHeight = height[high]
            else:
                maxHeight = height[high]
                minHeight = height[low]
            area = minHeight * (high - low)
            maxArea = max(area, maxArea)
            if maxHeight == height[high]:
                low += 1
            elif maxHeight == height[low]:
                high -= 1

        return maxArea
