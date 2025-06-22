import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def k_works(k):
            hours = 0
            for i in piles:
                hours += math.ceil((float(i)) / k)
            return hours <= h

        l = 1
        r = max(piles)
        res = float("inf")
        while l <= r:
            k = (l + r) // 2
            if k_works(k):
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
