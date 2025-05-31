class Solution(object):
    def trap(self, height):
        L_wall = R_wall = 0
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n

        for i in range(len(height)):
            j = -i - 1
            maxLeft[i] = L_wall
            maxRight[j] = R_wall

            L_wall = max(L_wall, height[i])
            R_wall = max(R_wall, height[j])

        sum = 0
        for i in range(len(height)):
            possible = min(maxLeft[i], maxRight[i])
            sum += max(0, possible - height[i])

        return sum
