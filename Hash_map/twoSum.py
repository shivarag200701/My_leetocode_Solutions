class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}  # value : index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [i, prevMap[diff]]
            prevMap[num] = i
