class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        r = n-1
        while(l<r):
            m = (l+r)//2
            if nums[m]>nums[r]:
                l = m + 1
            else:
                r = m
        min = l

        if nums[min]==target:
            return min
        l = 0
        r = n-1
        if target <= nums[r]:
            l = min+1
        else:
            r = min-1
        
        while(l<=r):
            m = (l+r)//2
            if target<nums[m]:
                r=m-1
            elif target>nums[m]:
                l=m+1
            else:
                return m
        return -1