class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = 0
        j = 0
        sum = 0
        minLen = float("inf")
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                minLen = min(minLen, j - i + 1)
                sum -= nums[i]
                i += 1

        if minLen == float("inf"):
            return 0
        else:
            return minLen
