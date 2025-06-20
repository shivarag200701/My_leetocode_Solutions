class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        sum = 0
        while sum != 1:
            seen.add(n)
            n = [int(num) for num in str(n)]
            sum = 0
            for i in n:
                sum += i * i
            n = sum
            if n in seen and n != 1:
                return False

        return True
