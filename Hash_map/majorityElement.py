class Solution(object):
    def majorityElement(self, nums):
        map1 = {}
        map2 = {}
        for i in nums:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] += 1

        for i in map1:
            if map1[i] not in map2:
                map2[map1[i]] = i

        return map2[max(map2.keys())]
