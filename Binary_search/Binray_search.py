class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = n - 1

        while i <= j:
            mid = i + (j - i) // 2  # Calculate mid correctly

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1

        return -1  # Target not found