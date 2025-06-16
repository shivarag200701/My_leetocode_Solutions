class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        found = False
        i = 0
        j = n - 1
        mid = (j - i) // 2
        # print(mid)
        while not found:
            if target > nums[mid]:
                i = mid + 1
                mid = i + (j - i) // 2
            elif target < nums[mid]:
                j = mid - 1
                mid = j - (j - i) // 2
            else:
                found = True

            if j < i:
                return -1

        return mid
