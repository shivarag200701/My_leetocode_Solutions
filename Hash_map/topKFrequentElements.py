class Solution(object):
    def topKFrequent(self, nums, k):
        map1 = {}
        map2 = {}
        for i in nums:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] += 1

        for i in map1:
            if map1[i] not in map2:
                map2[map1[i]] = [i]
            else:
                map2[map1[i]].append(i)

        res = []
        for freq in sorted(map2.keys(), reverse=True):
            for num in map2[freq]:
                res.append(num)
                if len(res) == k:
                    return res
