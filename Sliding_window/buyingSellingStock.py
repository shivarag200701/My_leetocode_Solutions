class Solution(object):
    def maxProfit(self, prices):
        ##easy
        n = len(prices)
        maxProfit = 0
        left = 0
        right = n - 1
        while left < right:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)

            if profit < 0:
                left += 1
            else:
                right -= 1

        return maxProfit
