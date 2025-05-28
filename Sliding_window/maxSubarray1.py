class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        windowSum = sum(nums[:k])
        maxSum = windowSum
        i = 0
        while k + i < n:
            windowSum = windowSum - nums[i] + nums[k + i]
            maxSum = max(maxSum, windowSum)
            i += 1

        return float(maxSum) / k
