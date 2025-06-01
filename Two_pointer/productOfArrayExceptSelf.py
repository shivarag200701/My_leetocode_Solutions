class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        leftProduct = [0] * n
        rightProduct = [0] * n
        res = [0] * n
        left = right = 1
        for i in range(n):
            j = -i - 1
            leftProduct[i] = left
            rightProduct[j] = right

            left *= nums[i]
            right *= nums[j]

        for i in range(n):
            res[i] = leftProduct[i] * rightProduct[i]

        return res
