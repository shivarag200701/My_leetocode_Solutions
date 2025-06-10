from collections import Counter, defaultdict


class Solution(object):
    def frequencySort(self, nums):
        count = Counter(nums)
        freqMap = defaultdict(list)
        for num in count:
            freq = count[num]
            freqMap[freq].append(num)

        res = []
        for i in sorted(freqMap):
            for j in sorted(freqMap[i], reverse=True):
                res += [j] * i

        return res
