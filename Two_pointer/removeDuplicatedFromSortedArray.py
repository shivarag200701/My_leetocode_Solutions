class Solution(object):
    def removeDuplicates(self, nums):
        unique = set()
        count = 0
        for i in nums:
            if i not in unique:
                unique.add(i)
                nums[count] = i
                count += 1

        return count
